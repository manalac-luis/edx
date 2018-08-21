#Uses python3

import sys

def max_dot_product(a, b):
    #write your code here
    res = 0

    matrix = []
    for i in range(len(a)):
        for j in range(len(b)):
            matrix.append([a[i]*b[j]])
    print(matrix)

    for i in range(len(a)):
        res += a[i] * b[i]
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print('a:',a)
    print('b:',b)
    print(max_dot_product(a, b))
