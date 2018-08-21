# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = 0
highest = 0
second  = 0

for i in range(0, n):
    if (a[i]>=highest):
        second = highest
        highest = a[i]
    elif (a[i]>=second):
        second = a[i]
#print("Highest", highest)
#print("Second ", second)
result = highest * second
print(result)
