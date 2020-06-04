import random
choosen = list(random.choice(['python', 'java', 'kotlin', 'javascript']))
print('H A N G M A N\n')
hidden = list('-' * len(choosen))
j = 0
while j < 8:
    print(''.join(hidden))
    guess = input('Input a letter: ')
    if guess in choosen:
        for i in range(len(choosen)):
            if choosen[i] == guess:
                hidden[i] = guess
        print()
    else:
        print('No such letter in the word\n')
    j += 1
print("""Thanks for playing!
We'll see how well you did in the next stage""")
