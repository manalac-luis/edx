# Uses python3
import sys

def get_change(m):
    tens = m // 10
    fives = (m - tens*10) // 5
    ones  = m - tens*10 - fives*5
    #write your code here
    return tens+fives+ones

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
