from random import randrange

def playGame():
    mysteryNumber = randrange(1, 10, 1)
    guesses_left = 3
    print("I have a number thaat ranges from 0-10\nWhat's my number?")
    while guesses_left != 0:
        guess = int(input("Enter your guess: "))
        if guess == mysteryNumber:
            print("Yay! You won\nThe number was ",str(mysteryNumber))
            return True
        else:
            guesses_left -= 1
            print("Opps sorry :(\nGuesses remaning:",str(guesses_left),"\n")


ans = playGame()
if ans != True:
    print("Better Luck Next Time!")