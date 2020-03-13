from math import sqrt

print("Pythagoras solver")
print("Plesae enter 0 for any values you don't have")

r = float(input("Enter the value of r: "))
x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

r_squared = pow(r,2)
x_squared = pow(x,2)
y_squared = pow(y,2)

if r == 0:
    r = sqrt(x_squared + y_squared)
    print("r =",r)
elif x == 0:
    x = sqrt(r_squared - y_squared)
    print("x =",x)
elif y == 0:
    y = sqrt(r_squared - x_squared)
    print("y =",y)
else: 
    print("The program unfortunately crashed")