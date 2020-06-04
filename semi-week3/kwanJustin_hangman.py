import random

word_list = ['python', 'java', 'kotlin','javascript']
lower_case_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print("H A N G M A N")

while True:
    start = input('Type "play" to play the game, "exit" to quit: ')
    if start == "play" or start == "exit":
        if start == "exit":
            break
        else:
            correct_word = random.choice(word_list)
            letters_list =  list(correct_word)
            correct_list = list(len(correct_word) * "-")
            guessed_list = []
            lives_count = 0

            print("")
            print(''.join(correct_list))
            while lives_count < 8:
                letter = input("Input a letter: ")
                if len(letter) == 1:
                    if letter in lower_case_letters:
                        if letter in guessed_list:
                            print("You already typed this letter\n")
                        else:
                            guessed_list.append(letter)
                            if letter in letters_list:
                                for i in range(len(letters_list)):
                                    if letters_list[i] == letter:
                                        correct_list[i] = letter
                                print("")
                                if correct_list == letters_list:
                                    print(''.join(correct_list))
                                    break                                    
                            else:
                                if lives_count < 7:
                                    print("No such letter in the word\n")
                                else:
                                    print("No such letter in the word")
                                lives_count += 1
                    else:
                        print("It is not an ASCII lowercase letter\n")
                else:
                    print("You should input a single letter\n")

                if lives_count < 8:
                    print(''.join(correct_list))
                
            if correct_list == letters_list:
                print(f"You guessed the word {correct_word}!")
                print("You survived!")
            else:
                print("You are hanged!")

            print("")
