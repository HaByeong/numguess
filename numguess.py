from random import randint
from time import sleep
def start_line():
  #Make answer
  answer=randint(1,100)
  #Get user_name
  user_name=input("What is your name?")
  print(f"Hi!, {user_name}! Please be my guest!!")
  #Get and print User's guess
  guess=int(input(f"So {user_name}, Guess the number(1~100): "))
  return answer, user_name, guess

def compare_line(guess,answer):
  if guess == answer:
    for i in range(3):
      print('*****************')
      sleep(1)
    print(f"You got it right!!!! The answer is {answer}!!")
  elif(answer>guess):
    print(f"That's too small..{user_name}")
    print(f"You lose~! So sad...answer is~~{answer}!")
  elif(answer<guess):
    print(f"That's too big..{user_name}")
    print(f"You lose~! So sad...answer is~~{answer}!") 
