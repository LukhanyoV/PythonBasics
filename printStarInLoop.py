#tart pattern in python
print("""
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*
""")


for i in range(1, 6, 1):
    print("*"*i)
for j in range(6, 0, -1):
    print("*"*j)
