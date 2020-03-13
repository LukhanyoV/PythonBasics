fname = input("Enter your first name: ")
lname = input("Enter your surname: ")
mark = int(input("Enter your grade: "))
fullName = fname +" "+ lname

if 80 <= mark and mark <= 100:
    print(fullName,"=> Grade A - Outstanding")
elif 60 <= mark and mark <= 79:
    print(fullName,"=> Grade B - Satisfactory")
elif 50 <= mark and mark <= 59:
    print(fullName,"=> Grade C - Pass")
elif 0 <= mark and mark <= 49:
    print(fullName,"=> Grade D - Fail")
else:
    print("Your",mark,"doesn't fit the required range!")