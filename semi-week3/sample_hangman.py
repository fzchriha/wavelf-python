import random

word_list = ('python', 'java', 'kotlin','javascript')

print("H A N G M A N")

def play_game():
  start = input('Type "play" to play the game, "exit" to quit: ')
  while start == "play" and start != "exit":
    correct_word = random.choice(word_list)
    letters_list =  list(correct_word)
    correct_list = list(len(correct_word) * "-")
    guessed_list = []
    lives_count = 0
    print("")
    print(''.join(correct_list))
    while lives_count < 8:
      letter = input("Input a letter: ")
      if len(letter) != 1:
        print("You should input a single letter\n")
      elif not letter.islower():
        print("It is not an ASCII lowercase letter\n")
      elif letter in guessed_list:
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
          
      if lives_count < 8:
        print(''.join(correct_list))
                  
    if correct_list == letters_list:
      print(f"You guessed the word {correct_word}!")
      print("You survived!")
    else:
      print("You are hanged!")

    print("")
    start = input('Type "play" to play the game, "exit" to quit: ')

play_game()
