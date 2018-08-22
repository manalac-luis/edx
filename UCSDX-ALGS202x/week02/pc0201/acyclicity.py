#Uses python3
# Python program to detect cycle
# in a graph
#https://www.geeksforgeeks.org/detect-cycle-in-a-graph/


import sys
from collections import defaultdict

class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        for i in range(vertices):
            self.graph[i]=[]
        self.V = vertices
        #print("self.graph",self.graph)

    def addEdge(self,u,v):
        self.graph[u].append(v)
        #print("self.graph",self.graph)

    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and
        # adds to recursion stack
        #print("v:",v)
        #print("size of visited:",len(visited))
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


def acyclic(n,edges):
    #n = len(edges)
    g = Graph(n)

    for i in range(len(edges)):
        g.addEdge(edges[i][0], edges[i][1])
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

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #print("input",input)
    #print("data:",data)
    n, m = data[0:2]
    d_edges=[]

    if m>n:
        n=m
    for i in range(1,len(data)//2):
        edge = [data[i*2],data[(i*2)+1]]
        d_edges.append(edge)

    print(acyclic(n,d_edges))
