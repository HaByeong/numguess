from random import shuffle, choice
result={
    'stay_to_win': 0,
    'move_to_win': 0,
}
door=[0,0,1]#:goat, 1:sports car
shuffle(door)
user_choice=choice(door)
if user_chioce==0:
    result['move_to_win']+=1
else:
    result['stay_to_win']+=1
print(result)
