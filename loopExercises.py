
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