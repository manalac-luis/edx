#Uses python3
import sys
import math


def distance(i,j,x,y):
    d = (x[i]-x[j])**2 + (y[i]-y[j])**2
    return math.sqrt(d)

def minimum_distance(x, y):
    #x is an array xi = x coordinate of node i
    #y is an array yi = y coordinate of node i
    n = len (x) #number of vertices

    #create adjency matrix

    adj = []

    for i in range(n):
        adj.append([None]*n)
        #print(adj[i])


    # Create an adjaceny matrix where i,j is the cost going from node i to j
    for i in range(n):
        for j in range(n):
            adj[i][j]= distance(i,j,x,y)

    #print("Adjancency Matrix")
    #for i in range(n):
    #    print(adj[i])

    #Initialize an empty array of known vertices K and known Segments P
    K = []
    P = []
    MSTval = 0

    #Add node 1 into K
    K.append(0)

    #Loop until all all vertices are in K
    while (len(K)<n):
            #Loop through all edges out of K, and select
            #edge with lowest cost going to a vertex not in K
            S = []
            C = []
            CD = []
            segment = -10000
            for i in range(len(K)):
                for j in range(n):
                    if (j not in K):
                        #print(j," not in K")
                        S.append(K[i])
                        C.append(j)
                        CD.append(adj[K[i]][j])
            #pick lowest edge
            #print("S:",S)
            #print("C:",C)
            #print("CD:",CD)
            min = 999999999
            path= ""
            index = -1

            for i in range(len(S)):
                if (CD[i]<min) and CD[i]>0:
                    min = CD[i]
                    path = str(S[i])+"-"+str(C[i])
                    index = i
                    segment = min
            #print("Path: ",path," Cost: ",min, " Index: ",index)
            if index>=0:
                K.append(C[index])
                P.append(path)
                MSTval = MSTval + segment
            else:
                K.append(-10000)

    #print("K:",K)
    #print("P:",P)
    #print("MSTval:",MSTval)

    #write your code here
    return MSTval

#Prim MST
# 1. Create an adjaceny matrix where i,j is the cost going from node i to j
# 2. Initialize an empty array of known vertices, K
# 3. Add node 1 into K
# 4. Loop until all all vertices are in K
# 4A.   Look through all vertices in K and select i,j such that
#          Vj is not in K, and CIJ is the lowest
#          Add Vj to K
#          Add RIJ to
# Done

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

    #Sample 1
    n = 4
    x = [0, 0, 1, 1]
    y = [0, 1, 0, 1]
    #print(minimum_distance(x,y))

    #Sample 2
    n = 5
    x = [0, 0, 1, 3, 3]
    y = [0, 2, 1, 0, 2]
    #print(minimum_distance(x,y))
