from random import randrange

mysteryNumber = randrange(1, 10, 1)
guesses_left = 3
print("I have a number thaat ranges from 0-10\nWhat's my number?")
while True:
    guess = int(input("Enter your guess: "))
    if guess == mysteryNumber:
        print("Yay! You won\nThe number was ",str(mysteryNumber))
        break
    else:
        guesses_left -= 1
        print("Opps sorry :(\nGuesses remaning:",str(guesses_left),"\n")

    if guesses_left == 0:
        print("Better Luck Next Time!"+"\nThe number was: "+str(mysteryNumber))
        break
