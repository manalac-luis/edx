# Uses python3
import sys


def merge(a,b):
    #merge 2 sorted arrays
    sorted = []
    ai = 0
    bi = 0
    #print("merge a:",a)
    #print("merge b:",b)
    inversion = 0
    for i in range(len(a)+len(b)):

        while ai<len(a) or bi<len(b):
            if ai>=len(a):
                sorted.append(b[bi])
                bi = bi+1
                break
            if bi>=len(b):
                sorted.append(a[ai])
                ai = ai+1



                break
            if (a[ai]<=b[bi]):
                sorted.append(a[ai])
                ai = ai+1
            else:
                sorted.append(b[bi])
                bi = bi+1






    inversion = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i]>b[j]:
                inversion = inversion+1
    #
    #print("merge sorted:",sorted," ",inversion)
    return(sorted,inversion)


def merge_sort(a):
    if len(a)==1:
        return(a,0)
    else:
        left  = merge_sort(a[0:len(a)//2])
        right = merge_sort(a[(len(a)//2):len(a)])
        #print("left:", left)
        #print("right:", right)
        #sorted = left[0]+right[0]
        #sorted.append(right[0])
        sorted = merge(left[0],right[0])
        inversions = sorted[1]+left[1]+right[1]
        #print("sorted:",sorted[0],",",inversions)
        return(sorted[0],inversions)

def inversions_naive(a):
    inversions = 0
    for i in range(len(a)):
        #print("i",i)
        val = a[i]
        for j in range(i+1,len(a)):
            if a[j]<val:
                inversions = inversions + 1
    return (inversions)

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = inversions_naive(a)
    return number_of_inversions

    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    return number_of_inversions

def mergeSort(alist):
    count = 0
    leftcount = 0
    rightcount = 0
    blist = []
    #print("mergeSort:",alist)

    if len(alist)>1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        leftcount, lefthalf = mergeSort(lefthalf)
        rightcount, righthalf = mergeSort(righthalf)

        i = 0
        j = 0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                blist.append(lefthalf[i])
                i += 1
            else:
                blist.append(righthalf[j])
                j += 1
                count += len(lefthalf[i:])

        while i < len(lefthalf):
            blist.append(lefthalf[i])
            i += 1

        while j < len(righthalf):
            blist.append(righthalf[j])
            j += 1


    else:
        blist = alist[:]

    #print("mergeSort:",count+leftcount+rightcount,",",blist)
    return count+leftcount+rightcount,blist




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    #print("a:",a)
    #print("b:",b)

    #result = merge_sort(a)
    #print("inversions 1:",result[1])

    inversions, sorted = mergeSort(a)
    print(sorted)
    print(inversions)

    #result = mergeSort(a)
    #print("merge sort: ",result[0])
    #print("inversions:",result[1])


    #print("naive: ",get_number_of_inversions(a, b, 0, len(a)))
