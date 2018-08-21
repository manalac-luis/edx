# Uses python3
import sys

def min(a,b,c):
    if (a<=b) and (a<=c):
        return(a)
    if (b<=a) and (b<=c):
        return(b)
    if (c<=a) and (c<=b):
        return(c)

def knapsack(W, B):
    #write your code here
    # W - capacity of knapsack
    # B - array of gold bars
    #print("Knapsack:", W)
    #print("Bars:",B)

    Matrix = [[0 for w in range(W+1)] for i in range(len(B)+1)]

    for i in range(1,len(B)+1):
        for w in range(1,W+1):
            Matrix[i][w] = Matrix[i-1][w]
            #print("B[i-1]",B[i-1])
            if B[i-1] <= w:
                val = Matrix[i-1][w-B[i-1]] + B[i-1]
                if Matrix[i][w]< val:
                    Matrix[i][w] = val

    #for i in range(len(B)+1):
        #print(Matrix[i])

    return Matrix[len(B)][W]


def optimal_weight(W, w):
    # write your code here
    result = 0
    for x in w:
        if result + x <= W:
            result = result + x
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
    print(knapsack(W,w))
