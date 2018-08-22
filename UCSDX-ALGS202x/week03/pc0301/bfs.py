#Uses python3
# Python program to detect cycle
# in a graph
#https://www.geeksforgeeks.org/topological-sorting/


import sys
from collections import defaultdict

class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        for i in range(vertices):
            #self.graph[i].append(-1000)
            self.graph[i]=[]
        self.V = vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)
        #print("self.graph",self.graph)
        #if undirected add reciprocal
    def addEdgeU(self,u,v):
        self.graph[u].append(v)
        #if undirected add reciprocal
        if u in self.graph[v]:
            print("")
        else:
            self.graph[v].append(u)


    def printAdj(self):
        for i in range(len(self.graph)):
            print("node: ",i+1," adj:",end="")
            for j in range(len(self.graph[i])):
                print(self.graph[i][j]+1," ",end="")
            print("")
 # Function to print a BFS of graph
    def BFS(self, s,v):

        #For all u element of V, mark distance as infinity
        dist = []
        for i in range(len(self.graph)):
            dist.append(999999999)
        #dist[s] = 0
        dist[s]=0


        #queue containing just s
        queue = []
        queue.append(s)
        #while queue not empty
        while (len(queue)>0):
            u = queue.pop(0)
            #get a vertex from the front of the queue
            #print("vertex:",u)

            for i in self.graph[u]:
                    if dist[i] > 1000000:
                        queue.append(i)
                        dist[i] = dist[u]+1
        #for i in range(len(dist)):
        #    print("dist:",i+1,",",dist[i])

        if (dist[v] > 1000000):
            return -1
        else:
            return dist[v]

        return dist[v]
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * self.V
        recStack = [False] * self.V
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node,visited,recStack) == True:
                    return True
        return False
    # A recursive function used by topologicalSort
    def topologicalSortUtil(self,v,visited,stack):

        # Mark the current node as visited.

        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)

        # Push current vertex to stack which stores result
        stack.insert(0,v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack =[]

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        #print("topologicalSort:", self.graph," ",self.V)
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)

        # Print contents of the stack
        for i in range(len(stack)):
            print (stack[i]+1," ",end="")
        print("")

def acyclic(n,edges):
    #n = len(edges)
    g = Graph(n)

    for i in range(len(edges)):
        g.addEdge(edges[i][0]-1, edges[i][1]-1)
        #print("Edges:",edges[i][0]," ",edges[i][1])
    #g.addEdge(1,2)
    #g.addEdge(4,1)
    #g.addEdge(2,3)
    #g.addEdge(3,1)

    if g.isCyclic() == 1:
        #print ("Graph has a cycle")
        return 1
    else:
        #print ("Graph has no cycle")
        return 0

def topo(n,edges):
    #n - number of vertices
    #edges - adjency list
    #n = len(edges)
    g = Graph(n)

    for i in range(len(edges)):
        g.addEdge(edges[i][0]-1, edges[i][1]-1)

    g.topologicalSort()

def bfs(n,edges,a,v):
    #n - number of vertices
    #edges - adjency list
    #a -starting vertex

    g = Graph(n)
    a = a - 1
    v = v - 1
    for i in range(len(edges)):
        g.addEdgeU(edges[i][0]-1, edges[i][1]-1)

    #g.printAdj();
    return(g.BFS(a,v))



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #print("input",input)
    #print("data:",data)
    n, m = data[0:2]
    d_edges=[]
    for i in range(1,m+1):
        edge = [data[i*2],data[(i*2)+1]]
        d_edges.append(edge)
    u, v = data[(m+1)*2:(m+1)*2+2]
    #print("u,v",u,",",v)

    print(bfs(n,d_edges,u,v))
