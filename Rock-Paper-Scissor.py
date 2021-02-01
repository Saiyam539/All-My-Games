import random
def gamewin(computer,player):
    if computer==player:
        return None

    elif computer == 'r':
        if player=='p':
            return True
        elif player=='s':
            return False
    
    elif computer == 'p':
        if player=='r':
            return False
        elif player=='s':
            return True

    elif computer=='s':
        if player=='p':
            return False
        elif player=='r':
            return True


print("Computer's turn:- Rock(r), Paper(p) and scissors(s)")
randnum = random.randint(1,3)
if randnum==1:
    computer= 'r'
elif randnum==2:
    computer = 'p'
elif randnum==3:
    computer = 's'


player = input("Players turn:- Rock(r), Paper(p) and scissors(s) ")
a = gamewin(computer,player)

print(f"Computer choose:- {computer}")
print(f"You choose:- {player}")


if a == None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")