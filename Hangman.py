import random

wordpossibility = ("gold", "silver", "bronze", "platinum", "diamond",
                   "emerald", "ruby", "sapphire", "amethyst", "topaz", "jade",
                   "opal", "moonstone", "pearl")


def displayed_word(word, guessed_letters):
  display = ""
  for letter in word:
    if letter in guessed_letters:
      display += letter + " "
    else:
      display += "_ "
  return display.strip()


def start_game():
  word = random.choice(wordpossibility)
  print("Welcome to the word guessing game!")
  print("You have 5 guesses to guess the word.")
  print("Press enter to begin")
  input()
  print("The word is", len(word), "letters long")

  guessed_letters = []
  correct_guesses = 0
  incorrect_guesses = 0
  while incorrect_guesses < 6 and "_" in displayed_word(word, guessed_letters):
    guess = input("Guess a letter or the whole word: ")
    if len(guess) == 1:
      if guess in guessed_letters:
        print("You already guessed that letter!")
      elif guess in word:
        guessed_letters.append(guess)
        correct_guesses += 1
        print("The letter", guess, "is in the word")
        print("Current word:", displayed_word(word, guessed_letters))
      else:
        print("Incorrect guess")
        incorrect_guesses += 1
        print("Current word:", displayed_word(word, guessed_letters))
        if incorrect_guesses == 1:
          print("  |  \n  |  \n  |  \n  |  \n  |  \n  |  \n__|__\n")
        elif incorrect_guesses == 2:
          print("  |----\n  |  \n  |  \n  |  \n  |  \n  |  \n__|__\n")
        elif incorrect_guesses == 3:
          print("  |----\n  |   o\n  |  \n  |  \n  |  \n  |  \n__|__\n")
        elif incorrect_guesses == 4:
          print("  |----\n  |   o\n  |   |\n  |  \n  |  \n  |  \n__|__\n")
        elif incorrect_guesses == 5:
          print("  |----\n  |   o\n  |  /|\\\n  |   |\n  |  \n  |  \n__|__\n")
        else:
          print(
              "  |----\n  |   o\n  |  /|\\\n  |   |\n  |  / \\\n  |  \n__|__\n"
          )
    else:
      if guess == word:
        correct_guesses += 1
        print("NICE! You guessed the word:", word, "in",
              correct_guesses + incorrect_guesses, "guesses")
        return
      

  if "_" not in displayed_word(word, guessed_letters):
    print("NICE! You guessed the word:", word, "in",
          correct_guesses + incorrect_guesses, "guesses")
  else:
    print("Out of guesses! The word was:", word)


start_game()