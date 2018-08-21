#Uses python3

import sys

def isGreaterOrEqual(a,b):
    #convert to padded string
    aS = str(a)
    bS = str(b)

    if len(aS)>=len(bS):
        lS = len(aS)
    else:
        lS = len(bS)

    aS=aS+"9999999"
    bS=bS+"9999999"
    aS = aS[:lS]
    bS = bS[:lS]
    #print ("aS,bS:",aS,",",bS)
    return (int(aS)>=int(bS))

def largest(a):
    answer = ""
    digits = a
    while (len(digits)>0):
        maxDigit = -1000
        index = -1
        for i in range(len(digits)):
            if isGreaterOrEqual(int(digits[i]),maxDigit):
                maxDigit = int(digits[i])
                index = i

        if (index>=0):
            #print("I:",i,maxDigit)
            digits.pop(index)
            answer = answer+str(maxDigit)

    return (answer)



if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest(a))
