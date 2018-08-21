# Uses python3
import sys

def DPChange(money,coins):
    #write your code here
    MinNumCoins = []
    #Initialize Array
    for i in range(money+1):
        MinNumCoins.append(1000000)
    MinNumCoins[0]= 0

    for m in range(1,money+1):
        MinNumCoins[m] = 1000000
        for i in range(len(coins)):
            if m >= coins[i]:
                NumCoins = MinNumCoins[m-coins[i]]+1
                if NumCoins < MinNumCoins[m]:
                    MinNumCoins[m]=NumCoins
    #print("money,MinNumCoins:",money,",",MinNumCoins[money])
    return MinNumCoins[money]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    #print(get_change(m))
    print(DPChange(m,[1,3,4]))
