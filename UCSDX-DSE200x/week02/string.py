word = ' Hello '

word1 = word.lower()

print(word1)

word2 = word.upper()

print(word2)

print(word1+" "+word2)

#Replication

print(word1*2)

#Remove leading and trailing spaces or other characters

word3 = word.strip()

print(word3)

#split

word4 = word1+" "+word2
array4 = word4.split(" ")
print(array4)

#slicing

word5 = word2.strip()
print(word5)
print(word5[1:3])
print(word5[4:7])
print(word5[-4:-1])

#Substtring Testing

print('HE' in word5)
print("He" in word5)
print(word5.find("EL"))
print(word5.find("el"))

#Convert to Nmber

word6 = "1234"
print (int(word6))
print (float(word6))
#print (int(word5))

#String Formatting
statement = "We love {0} {1}"
print(statement.format("data","analysis"))
