
#print even number from 100 t0 2
number1 = 100
while number1 >= 2:
    print(number1,"is even!")
    number1 -= 2

print("\n\n")

# multiplication table
userNumber = int(input("Enter number: "))
number2 = 1
ans = 0
while number2 <= 10:
    ans = userNumber * number2
    print(str(userNumber)+" * "+str(number2)+" = "+str(ans))
    number2 += 1


# capture names and store in a list
myNames = []
count = 10
while count != 0:
    name = input("Please enter a name: ")
    myNames.append(name)
    count -= 1

# print names in a list
count = len(myNames)
i = 0
while i < count:
    print(myNames[i])
    i += 1
