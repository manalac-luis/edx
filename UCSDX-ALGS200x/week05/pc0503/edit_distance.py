# Uses python3
# Additional Edit Distance Tutorial
# https://www.youtube.com/watch?v=We3YDTzNXEk
def min(a,b,c):
    if (a<=b) and (a<=c):
        return(a)
    if (b<=a) and (b<=c):
        return(b)
    if (c<=a) and (c<=b):
        return(c)

def edit_distance(s, t):
    #write your code here
    # len(s)+1 items
    # len(t)+1 elements
    Matrix = [[0 for x in range(len(t)+1)] for y in range(len(s)+1)]

    for y in range(len(s)+1):
        for x in range(len(t)+1):
            Matrix[0][x]=x
            Matrix[y][0]=y
            if y>0 and x>0 :
                i = Matrix[y-1][x]+1
                d = Matrix[y][x-1]+1
                m = Matrix[y-1][x-1]
                sb = Matrix[y-1][x-1]+1

                if s[y-1]==t[x-1]:
                    #print("Match")
                    val = min(i,d,m)
                else:
                    #print("No Match")
                    val = min(i,d,sb)
                Matrix[y][x]=val

    #for y in range(len(s)+1):
        #print(Matrix[y])

    return Matrix[len(s)][len(t)]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
