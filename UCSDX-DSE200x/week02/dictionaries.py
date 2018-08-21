dict = { ('Ghostbusters',2016):5.4,
('Ghostbusters',1984):7.8}

print(dict)

print(dict[('Ghostbusters',2016)])
print(len(dict))

dict[('Cars',2006)] = 7.1

print(dict)

#remove an item from the dictionary

dict.pop(('Ghostbusters',2016))

print(dict)

for i in dict:
    print(i)
    
for key, value in dict.items():
    print (key,":",value)
