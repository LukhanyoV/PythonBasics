
n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

if n1 > n2 > n3:
  print(n1)
elif n1 > n3 > n2:
  print(n1)
elif n2 > n1 > n3:
  print(n2)
elif n2 > n3 > n1:
  print(n2)
elif n3 > n2 > n1:
  print(n3)
elif n3 > n1 > n2:
  print(n3)
else:
  print("ALL NUMBERS ARE EQUAL")
  
  
