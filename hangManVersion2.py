from os import system

#initialise something here
word = "Mbulelo"
wList = []
cList = []
xList = []
rList = []
count = 5
answer = ""

#turn word to a list
for i in word:
    wList.append(i)
    rList.append(i)

while len(wList) != 0 or count != 0:
    gList = []
    system("clear")

    print(answer)
    print("Counter:",count)
    for letter in rList:
        if letter not in cList:
            gList.append("*")
        else:
            gList.append(letter)
    print("Word List:",gList)
            
    print("Letters remaining:",len(wList))
    print("Letters correctly answered:",cList)
    print("Letters incorrectly guessed:",xList)


    
    uIn = input("\nEnter your letter: ")  
    if uIn in wList:
        answer = "Yay you got it right"
        while uIn in wList:
            wList.remove(uIn)
        cList.append(uIn)
    else:
        answer = "Nay you got it wrong"
        xList.append(uIn)
        count -= 1

    if len(wList) == 0:
        print("\n\nYAY YOU WON\n\n")
        break

    if count == 0:
        print("\n\nTHE GAME IS OVER\n\n")
        break
        
