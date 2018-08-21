list = [11,22,33]

list.append(44)

print(list)

for i in list:
    print(i)

for i in range(0,len(list)):
    print(list[i])

#lists are mutable and resizeable

list[0] = 10

for i in list:
    print(i)

#pop -- remove by index
#remove -- remove by value

list = [1, 2, 3]
list2= [4, 5, 6]

list.extend(list2)

print(list)

#zip

for x,y in zip(list, list2):
    print (x,",",y)
