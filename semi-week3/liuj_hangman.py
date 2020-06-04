import random

list1 = ['python', 'java', 'kotlin', 'javascript']
index = random.randint(0, 3)
word = list1[index]
listWord = list(word)
hyphen = "-"*len(word)
alreadyGuessed = []
listHyphens = list(hyphen[0:len(word)])
loopContinue = True
tries = 8
print("""H A N G M A N\n""")
userInput = input('Type "play" to play the game, "exit" to quit:')
if userInput == 'play':
   while(loopContinue):
     print()
     print("".join(listHyphens))
     userInput = input(("Input a letter: "))
     if userInput.islower():
        if len(userInput) == 1:
           if userInput not in alreadyGuessed:
              if (userInput in listWord):
                 replacement = listWord.index(userInput)
                 i=1
                 while i<listWord.count(userInput):
                    listHyphens[replacement] = userInput
                    listWord[replacement]=None
                    replacement = listWord.index(userInput)
                    listHyphens[replacement] = userInput
                    listWord[replacement]=None
                    i+=1
                 if i == 1:
                    listHyphens[replacement] = userInput
                    listWord[replacement]=None
                    i+=1
                 alreadyGuessed.append(userInput)
              else:
                 tries -= 1
                 print("No such letter in the word")
           else:
              print("You already typed this letter")
        else:
           print("You should input a single letter")
     else:
        print("It is not an ASCII lowercase letter")


     if (tries==0):
        loopContinue = False
     if (word == "".join(listHyphens)):
        loopContinue = False
     if (tries==0):
       loopContinue = False
     if (word == "".join(listHyphens)):
        loopContinue = False
   print("\nThanks for playing!\nWe'll see how well you did in the next stage")


