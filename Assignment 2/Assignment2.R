rm(list = ls())

lapply(c('optrees', 'igraph'), require, character.only = TRUE)      #, 'qgraph'

#############
##Functions##
#############
#Matrix Representation
AdjMatrix2List <- function(d){
  ds <- which(!is.na(d), arr.ind = T)
  ds <- as.matrix(ds)
  temp <- matrix(0, nrow = nrow(ds), ncol = 1)
  
  for (i in 1:nrow(ds)) {
    temp[i] <- d[ds[i,1], ds[i, 2]]
  }
  
  ds <- cbind(ds, temp)
  ds <- ds[,c(2, 1, 3)]
  colnames(ds) <- c('Source', 'End', 'weight')
  return(ds)
}

#Minimum Spanning Tree
plot.mst <- function(arcList) {
 for (i in 1:nrow(arcList)){
   x0 <- x[arcList[i,1]]
   y0 <- y[arcList[i,1]]
   x1 <- x[arcList[i,2]]
   y1 <- y[arcList[i,2]]
   segments(x0, y0, x1, y1)
 } 
}

#Problems
#Matrix Representation
n <- 1000
d <- runif(n*n)
d[d < 0.80] <- NA
d <- matrix(d, nrow = n, ncol = n)
diag(d) <- NA
d[upper.tri(d)] = t(d)[upper.tri(d)]    #upper.tri is upper triangle of a matrix and t is matrix transpose



#Minimum Spanning Tree
n <- 25
x <- round(runif(n) * 1000)
y <- round(runif(n) * 1000)
plot(x, y, pch = 16)

d <- matrix(0, nrow = n, ncol = n)   #initialize sparse matrix
matrixy <- as.matrix(y)
matrixx <- as.matrix(x)

for (i in 1:length(x)) {
  matrow <- sqrt(((x[i] - matrixx)^2) + ((y[i] - matrixy) ^ 2))
  d[i,] <- matrow
}

ds <- AdjMatrix2List(d)

ds.mst <- msTreePrim(1:n, ds)
plot.mst(ds.mst$tree.arcs)



#Hostile Agents

#4.1: Shortest path problem
#     Get from source node(start spy) to end node(receiving spy) while minimizing the cost(probability of getting caught) of doing so
#     Any edge weights would be the probability of getting caught

#4.2: Inputs would be -log(1 - p(Getting Caught))

#4.3: Dijkstra's Algorithm as we are looking for a shortest path with no negative weights edges. i.e. no negative probability

#4.4: Runtime: O(Edge lg Vertices)



#Project Scheduling

s.labels <- c('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
s.nodes <- c(90, 15, 5, 20, 21, 25, 14, 28, 30, 45)

sneg.nodes <- s.nodes * -1

#create a matrix with estimated times from each node
adjmat <- matrix(NA, nrow = length(s.labels), ncol <- length(s.labels))
dimnames(adjmat) <- list(s.labels, s.labels)

adjmat[2, 1] <- 90
adjmat[3, 2] <- 15
adjmat[4, 7] <- 14
adjmat[5, 4] <- 20
adjmat[6, 1] <- 90
adjmat[7, 3] <- 5
adjmat[7, 6] <- 25
adjmat[8, 4] <- 20
adjmat[9, 1] <- 90
adjmat[10, 4] <- 20
adjmat[10, 9] <- 30

adjlist <- AdjMatrix2List(adjmat * -1)

short <- getShortestPathTree(1:length(s.labels), adjlist, 'Bellman-Ford', show.data = FALSE, show.distances = FALSE, show.graph = FALSE)
dist <- matrix(0, nrow = length(s.labels), ncol = 1)
dist[,1] <- (short$distances * -1)
dist <- data.frame(dist)
date <- rep(as.Date('2017-11-1'), ncol(dist))
dist <- cbind(dist, date)
dist[,2] <- dist[,2] + dist[,1]
EF <- dist[,1] + s.nodes
dist[,3] <- EF
dist[,4] <- dist[,3] + dist[,2]
rownames(dist) <- s.labels
colnames(dist) <- c(' ES Days','ES Date', 'EF Days', 'EF Date')

adjmatT <- matrix(NA, nrow = length(s.labels) + 1, ncol = length(s.labels) + 1)
t.labels <- c('dum' ,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
t.nodes <- c(0, 90, 15, 5, 20, 21, 25, 14, 28, 30, 45)
dimnames(adjmatT) <- list(t.labels, t.labels)

adjmatT[11, 1] <- 0
adjmatT[9, 1] <- 0
adjmatT[6, 1] <- 0
adjmatT[5, 11] <- 45
adjmatT[10, 11] <- 45
adjmatT[2, 10] <- 30
adjmatT[5, 9] <- 28
adjmatT[4, 8] <- 14
adjmatT[7, 8] <- 14
adjmatT[2, 7] <- 25
adjmatT[5, 6] <- 21
adjmatT[8, 5] <- 20
adjmatT[3, 4] <- 5
adjmatT[2, 3] <- 15

adjlistT <- AdjMatrix2List(adjmatT * -1)

shortT <- getShortestPathTree(1:length(t.labels), adjlistT, 'Bellman-Ford', show.data = FALSE, show.distances = FALSE, show.graph = FALSE)
distT <- shortT$distances[-1]
dist[,5] <- distT * -1


LFdays <- ((distT * -1) - 194) * -1
dist[,5] <- LFdays
dist[,6] <- dist[,5] - s.nodes
dist[,7] <- LFdays - dist[,3]
colnames(dist) <- c(' ES Days','ES Date', 'EF Days', 'EF Date', 'LF Days', 'LS Start', 'Slack')
#B, C, E, H, I have flexibility
#A, D, F, G, J are on critical path