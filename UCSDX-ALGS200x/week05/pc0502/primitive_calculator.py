# Uses python3
import sys

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return reversed(sequence)

def calculate(n):
    MinNum = []
    PathNum = []
    #Initialize Array
    for i in range(n+1):
        MinNum.append(1000000)
        PathNum.append("")
    MinNum[0]= 0
    MinNum[1]= 0
    PathNum[0]= ""
    PathNum[1]="1"

    for m in range(2,n+1):
        op1 = MinNum[m-1]+1 #Default Case, use +1 Operator
        p1  = PathNum[m-1]+" "+str(m)
        if (m % 2 == 0):
            op2 = MinNum[ m // 2]+1
            p2 = PathNum[ m //2]+" "+str(m)
        else:
            op2 = 1000000
            p2 = ""

        if (m % 3 == 0):
            op3 = MinNum[ m // 3]+1
            p3 = PathNum[ m //3]+" "+str(m)
        else:
            op3 = 1000000
            p3 =""

        op = op1
        p = p1

        if op1 <= op2 and op1<= op3:
            op = op1
            p = p1
        elif op2<= op1 and op2<= op3:
            op = op2
            p = p2
        elif op3<= op1 and op3<= op2:
            op = op3
            p = p3
        PathNum[m] = p
        MinNum[m]= op
    #print("money,MinNumCoins:",money,",",MinNumCoins[money])
    return MinNum[n],PathNum[m]


input = sys.stdin.read()
n = int(input)
Min, Path = calculate(n)
print(Min)
print(Path)
#sequence = list(optimal_sequence(n))
#print(len(sequence) - 1)
#for x in sequence:
#    print(x, end=' ')
