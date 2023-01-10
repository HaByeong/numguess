from random import randint
from time import sleep
#Make answer
answer=randint(1,100)
#Think your user_num(1~100)
user_name=input("What's is your name?")

print(f"Hi!,{user_name}! Please be my guest!!")
#Get and print User's guess
guess = int(input(f"So {user_name}, Guess the number(1~100): "))
#Compare answer with user's guess
if guess == answer:
    print('*****************')
    sleep(1)
    print('*****************')
    sleep(1)
    print('*****************')
    sleep(1)
    print(f"You got it right!!!! The answer is {answer}!!")
elif(answer>guess):
  print(f"That's too small..{user_name}")
  print(f"You lose~! So sad...answer is~~{answer}!")
elif(answer<guess):
  print(f"That's too big..{user_name}")
  print(f"You lose~! So sad...answer is~~{answer}!")

