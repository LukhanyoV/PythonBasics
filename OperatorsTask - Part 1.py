
#given inputs
basic_salary = 1500
bonus_rate = 200
commision_rate = 0.02 # 2% = 2/100 = 0.02

#inputs from the end user
numberOfLaptops = float(input("Enter the number of laptops sold: \n"))
priceOfLaptops = float(input("Enter the price of the laptop: \n"))

#check if you qualify for the bonus
if priceOfLaptops > bonus_rate:
    #bonus for laptops sold
    bonus = bonus_rate * numberOfLaptops
else:
    bonus = 0

#commision for number of laptops sold
commision = commision_rate * numberOfLaptops * priceOfLaptops
#gross salary
gross_salary = basic_salary + commision + bonus

#the output convert the price to two decimal place
print("Bonus: R"+" "+str(round(float(bonus),2)))
print("Commision: R"+" "+str(round(float(commision),2)))
print("Gross Salary: R"+" "+str(round(float(gross_salary),2)))