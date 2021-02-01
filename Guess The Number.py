import random
randnum = random.randint(1,100)
userguess = None
guesses = 0

print('*****WELCOME TO THE SAIYAM GAME ZONE!!*****\n')

while(userguess != randnum):
    userguess = int(input('Enter the guess:- '))

    guesses += 1
    
    if userguess==randnum:
        print('Your guess is right!!')
    else:
        if userguess>randnum:
            print('you guessed it wrong, Enter the smaller number')
        else:
            print('You gussed it wrong Enter the larger number')

print(f'You guessed the number in {guesses} guesses')

