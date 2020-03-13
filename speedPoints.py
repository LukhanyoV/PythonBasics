#user speed
userSpeed = int(input("What was your average speed in km/h?"))

#allowed speed
allowedSpeed = int(input("What was the allowed speed on the road?"))

#round the user speed to the nearest 5
# def roundThis():
#     return 5 * round(userSpeed/5)


#get points
points = (-allowedSpeed + userSpeed)//5

# userSpeed = roundThis()

#check if driver gets points
if allowedSpeed > userSpeed:
    print("You are a good driver!")
elif points >= 12:
    print("Time to go to jail!")
else:
    print("Points:",points)