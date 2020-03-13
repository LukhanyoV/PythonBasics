
#what to convert
print("Input \"C\" if you want to convert to CelciuS\nInput \"F\" if you want to convert to Fahrenheit")

#user input
userInput = input("Please enter the units: ").lower().strip()

#check which conversion to do
if userInput == "c":
    fahrenheit = float(input("Enter your fahrenheit(without the units): \n"))
    celsius = 5/9 * fahrenheit - 32
    print(str(fahrenheit)+"F == "+str(round(celsius,1))+"C")
elif userInput == "f":
    celsius = float(input("Enter your celsius(without the units): \n"))
    fahrenheit = 9/5 * celsius + 32
    print(str(celsius)+ "C == " + str(round(fahrenheit,1))+"F")
else:
    print("fy")