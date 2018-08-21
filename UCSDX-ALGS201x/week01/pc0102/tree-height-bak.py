# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight2:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation


                maxHeight = 0
                for vertex in range(self.n):
                        height = 0
                        i = vertex
                        while i != -1:
                                height += 1
                                i = self.parent[i]
                        maxHeight = max(maxHeight, height);
                return maxHeight;

class TreeHeight:

        def __init__(self,size):
            self.treeArray = []
            self.distanceArray = []
            for i in range(size):
                self.treeArray.append(0)
                self.distanceArray.append(-1)

        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

        def compute_height(self):
                # Replace this code with a faster implementation
                for i in range(self.n):

                    if (self.parent[i]==-1):
                        root = i
                        self.distanceArray[root]=0
                        break;
                #compute distance from node to root

                for i in range(self.n):
                    distance = 0
                    if (i==root):
                        distance = 0
                        self.distanceArray[i]=0

                    else:
                        j = i
                        pathArray = []
                        distance =1
                        #Do While Parent is Not Root
                        while (self.parent[j]!=root):
                            pathArray.append(self.parent[j])
                            #if (self.distanceArray[self.parent[j]]!=-1):
                            if (False):
                                #print("Node",j,"Parent:",self.parent[j],"Distance:",self.distanceArray[self.parent[j]])
                                #print("Path",pathArray)
                                distance = distance+self.distanceArray[self.parent[j]]
                                self.distanceArray[j]=distance
                                break #get out of the while loop
                            else:
                                distance = distance+1
                                #self.distanceArray[j]=distance
                                #print("Node",j,"Parent:",self.parent[j],"Distance:",self.distanceArray[self.parent[j]])
                                #print("Path",pathArray)
                                j = self.parent[j]

                        self.distanceArray[i]=distance
                        print("Node",i,"Distance:",distance)
                        pdistance = 1
                        for i in range(len(pathArray)-1,-1,-1):
                            self.distanceArray[pathArray[i]]=pdistance
                            #print("Node:",pathArray[i]," Distance:",pdistance)
                            pdistance = pdistance+1
                        #print("Distance Array",self.distanceArray[:self.n])



                return max(self.distanceArray)+1



def main():
  tree = TreeHeight(1000000)
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
