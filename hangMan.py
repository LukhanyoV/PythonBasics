#initialise something here
word = "Lukhanyo"
wList = []

#turn word to a list
for i in word:
    wList.append(i)

def find(el):
    for i in wList:
        if el != i:
            return False
        else:
            return True

#the actual program
while len(wList) != 0 :
    uIn = input("Enter a letter: ")
    if find(uIn):
        print("Correct letter!")
        wList.remove(uIn)
    else:
        print("Incorrect letter!")
            