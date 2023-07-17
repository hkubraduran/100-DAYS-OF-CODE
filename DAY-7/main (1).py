#Step 1 
import random
import hangman_words
import hangman_art

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
print(hangman_art.logo)
random_num = random.randint(0,2) 
chosen_word = hangman_words.word_list[random_num]
#chosen_word = random.choice(word_list)
print(chosen_word)
length = len(chosen_word)
#create blanks
blank_list = [] 
for i in range(length):
  blank_list += "_"

end_of_game = False 
lives = 6

while  end_of_game == False:   #or while end_of_game == False
  
  guess = input("Guess a letter: ").lower()    #inside the while/for loop
  if guess in chosen_word:
    if guess in blank_list:
      print("You have already choosen that letter.")
    else: 
      for index in range(length) :
        if guess == chosen_word[index] : 
          blank_list[index] = guess
          
          if "_" not in blank_list:
            end_of_game == True
            print("You win.")
    
  else:
    lives -= 1 
    print(f"The letter {guess} is not in the word.")
    print(hangman_art.hang[lives])
    if lives == 0:
      end_of_game ==  True
      print("You lose.")

  print(blank_list)

  
  