#Uses python3
# Python program to detect cycle
# in a graph
#https://www.geeksforgeeks.org/topological-sorting/


import sys
from collections import defaultdict

class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v):
        self.graph[u].append(v)
        #print("self.graph",self.graph)

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
        #print("Edges:",edges[i][0]," ",edges[i][1]," ",i," ",n)
        g.addEdge(edges[i][0]-1, edges[i][1]-1)

    #g.addEdge(1,2)
    #g.addEdge(4,1)
    #g.addEdge(2,3)
    #g.addEdge(3,1)
    g.topologicalSort()




if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #print("input",input)
    #print("data:",data)
    n, m = data[0:2]
    d_edges=[]
    for i in range(1,len(data)//2):
        edge = [data[i*2],data[(i*2)+1]]
        d_edges.append(edge)

    topo(n,d_edges)
