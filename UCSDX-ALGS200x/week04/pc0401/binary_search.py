# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

def binary_search(a,x):

    min = 0
    max = len(a)-1
    mid = (min+max) //2
    if (a[min]==x):
        return(min)
    if (a[max]==x):
        return(max)
    while (True):
        mid = (max + min ) // 2
        #print("min, mid, max",min," ",mid," ",max)
        if a[mid] == x:
            #print("found:",mid)
            return(mid)
        elif a[mid]>x:
            max = mid
        else:
            min = mid
        #print("n.min, n.mid, n.max",min," ",mid," ",max)
        if (max-min<=1):
            return -1



if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]

    #print("n:",n)
    #print("m:",m)
    #print("a:",a)
    counter = 0

    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        #if (linear_search(a,x)>=0):
        if(binary_search(a,x)>=0):
            counter = counter+1
            print("x: ",x,"found")
        else:
            print("x: ",x,"not found")
        #print(linear_search(a, x), end = ' ')
    #linear search 49991
    print("Entries Found:",counter)
