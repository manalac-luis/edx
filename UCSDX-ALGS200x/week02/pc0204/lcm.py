# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd(a, b):
    if (b==0):
        return a
    else :
        aprime  = a % b
        return gcd(b,aprime)


#The least common multiple (lcm) of a and b is their product divided
#by their greatest common divisor (gcd) ( i.e. lcm(a, b) = ab/gcd(a,b)).

def lcm(a,b):
        return (((a*b)//gcd(a,b)))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))
