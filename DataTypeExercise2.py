#declare list
cars = [56,78,34,21,56,34,125,45,89,75,12,56]

#find the smallest number
smallNumber = min(cars)

#find the largest number
largeNumber = max(cars) 

#print smallest number 
print(smallNumber)

#print largest number
print(largeNumber)

#find the sum of all the numbers
sum = 0
for i in cars:
    sum += i

#print the sum of the two numbers
print(sum)

#find none dupliactes and append to a new list
newCars = []
for i in cars:
    if i not in newCars:
        newCars.append(i)
    
#make old cars be equal to new cars
cars = newCars

#print the corrected list
print(cars)