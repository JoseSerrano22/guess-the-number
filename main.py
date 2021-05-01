
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