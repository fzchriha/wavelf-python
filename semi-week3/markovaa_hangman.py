import random

def play():
    print("H A N G M A N\n")
    word_list = ["python", "java", "kotlin", "javascript"]
    hang_word = random.choice(word_list)
    tries = 1
    letters_tried = []
    letters_tried2 = []

    def get_hidden_word():
        hang_word_hidden = ""
        stars_to_add = len(hang_word)
        hang_word_hidden += ("- " * stars_to_add)
        return hang_word_hidden


    hidden_word = get_hidden_word().split()
    word_to_fill = [hidden_word]
    while tries != 9:
        str_word_to_fill = "".join(word_to_fill[0])
        print("\n", str_word_to_fill)
        guess_letter = input("Input a letter: ")
            
        if guess_letter not in letters_tried:
            letters_tried.append(guess_letter)
            
            
        if len(guess_letter) != 1: #Checks if only one letter was entered
            print("You should input a single letter")
            continue
        if guess_letter.isalpha():  # Check if the input is letter-only.
            pass
        else:
            print("It is not an ASCII lowercase letter")
            continue
            
            
        if guess_letter.islower(): #Checks if the letter is lowercase
            pass
        else:
            print("It is not an ASCII lowercase letter")
            continue
           
            
        if guess_letter in letters_tried2:
            print("You already typed this letter")
            continue


        if guess_letter in hang_word:
            for i in range(len(hidden_word)):
                if hang_word[i] == guess_letter:
                    word_to_fill[0][i] = guess_letter
                    if hang_word == hidden_word:
                        print("You guessed the word!")
        else:
            print("No such letter in the word")
            tries +=1
        if guess_letter not in letters_tried2:
            letters_tried2.append(guess_letter)

    if hang_word == hidden_word:
        print("You survived!")
    elif hang_word != hidden_word:
        print("You are hanged!")
    play_or_not = str(input('Type "play" to play the game, "exit" to quit:'))

play_or_not = str(input('Type "play" to play the game, "exit" to quit:'))
if play_or_not == 'exit':
    exit()
else:
    play()
