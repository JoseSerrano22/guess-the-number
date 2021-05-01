#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100")

dificulty = input("Choose a dificulty. Type 'easy' or 'hard': ").lower()

number_game = random.randint(1,100)

if dificulty == "easy":
  attempt = 10

  while attempt != 0:
    print(f"You have {attempt} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    if(guess == number_game):
      print("You win!")
      break
    else:
      if(guess < number_game):
        print("Too Low")
      elif(guess > number_game):
        print("Too High")
      attempt -= 1

elif dificulty == "hard":
  attempt = 5

  while attempt != 0:
    print(f"You have {attempt} attempts remaining to guess the number.")

    guess = int(input("Make a guess: "))

    if(guess == number_game):
      print("You win!")
      break
    else:
      if(guess < number_game):
        print("Too Low")
      elif(guess > number_game):
        print("Too High")
      attempt -= 1