#Uses python3

import sys

def find_path(graph, start, end, path=[]):
        #print("find_path",graph,start,end)
        path = path + [start]
        if start == end:
            return path
        if  not (start in graph):
            return None
        #    print("")
        #else:
        #    return None
        #if not graph.has_key(start):
        #    return None
        for node in graph[start]:
            if node not in path:
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

def make_graph(adj):
    d = {}
    for i in range(len(adj)):
        d[i]=adj[i]
    #print("d",d)
    return d

def reach(adj, x, y):
    #write your code here
    #adj is an arr[i] is an array of [xj...] indicating node xj+1 is adj to node i+1
    d_graph=make_graph(adj)

    d_path = find_path(d_graph,x,y)

    #print("reach: ",d_path)

    if (d_path==None):
        return(0)
    else:
        return(1)



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
