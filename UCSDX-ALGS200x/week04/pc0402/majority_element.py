# Uses python3
import sys

def is_majority(a,x):
    #is x a majority in a
    counter = 0
    for i in range(len(a)):
        if a[i]==x:
            counter = counter+1
    if (counter> len(a)/2):
        return counter
    else:
        return -1

def rec_majority(a):
    #print("rec_majority -> a:",a)
    if (len(a)==0):
        return(0,0)
    elif (len(a)==1):
        return(a[0],1)
    else:

        left = rec_majority(a[0:len(a)//2])
        right = rec_majority(a[(len(a)//2):len(a)])

        if (left[1]<0) and (right[1]<0):
            #print("no majority")
            return(0,0) # no majority

        if (left[1]>0) and (right[1]<0):
            #print("left majority: ",left)
            m = is_majority(a,left[0])
            if (m>=0):
                return(left[0],m)
            else:
                return(0,0)
        if (right[1]>0) and (left[1]<0):
            #print("right majority: ",right)
            m = is_majority(a,right[0])
            if (m>=0):
                return(right[0],m)
            else:
                return(0,0)
        #both left an right have is_majority
        #print("two majorities")
        m = is_majority(a,left[0])
        #print("l:",left[0]," ",m)
        if (m>=0):
            return(left[0],m)
        m = is_majority(a,right[0])
        #print("r:",right[0]," ",m)
        if (m>=0):
            return(right[0],m)
        #print("no majorites",a)
        return(0,0)




def get_majority_element(a, left, right):
    #print("a:",a)
    #print("left:",left)
    #print("right:",right)
    rec = rec_majority(a)
    print("rec:",rec)
    if (rec[1]==0):
        return 0
    else:
        return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_majority_element(a,0,n))
    #if get_majority_element(a, 0, n) != -1:
    #    print(1)
    #else:
    #    print(0)
