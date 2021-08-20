import random

EASY_TURNS = 10
HARD_TURNS = 5

def check_answer(guess,answer,turns):
  '''function gives the answer wheather it is high,low or corret'''
  if guess > answer:
    print("Too HIGH ")
    return turns-1
  elif guess < answer:
    print("Too LOW")
    return turns-1
  elif guess == answer:
    print("Hurray! you got it!")

def set_difficulty():
  level = input("choose your difficulty :'easy' or 'hard': ").lower()
  if level == "easy":
    return EASY_TURNS
  elif level == "hard":
    return HARD_TURNS

def play_game():

  print("WELCOME TO GUESS NUMBER GAME\n")
  print("THINKING NUMBER BETWEEN (1-100)\n")
  #make random number from 1-100
  answer = random.randint(0,100)
  
  #ask difficulty to a user
  turns = set_difficulty()

  

  guess=0
  while guess!=answer:

    print(f"you have {turns} attempts remaing to guess the number")

    #make a user guess
    guess = int(input("Tell me a number that I guess : "))
    turns = check_answer(guess,answer,turns)
    if turns == 0:
      print("your attempts are turned out")
      return
    elif guess != answer:
      print("guess again")
    

play_game()