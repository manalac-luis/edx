# Uses python3
#too slow
def calc_fib_slow(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib(n):
    if (n<=1):
        return n
    else:
        fib = [0,1]
        for i in range(2,n+1):
            #print(i)
            fib.append(fib[i-2]+fib[i-1])
        #print(fib)
        return (fib[n])

n = int(input())
print(calc_fib(n))
