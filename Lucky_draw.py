import datetime
import random
class luck_draw:
    @staticmethod
    def greeting():
        name = input('Enter your name here:- ')
        hour = int(datetime.datetime.now().hour)
        if hour>0 and hour<=12:
            print(f'Good Morning {name}')
        elif hour>12 and hour<=17:
            print(f'Good Afternoon {name}')        
        else:
            print(f'Good Evening {name}')
    @staticmethod
    def guess_number():
        print('YOU HAVE TO GUESS A NUMBER TO WIN')
        random_number = random.randint(1,10)
        print('Please guess a number from 1 to 10\n** If your guess is correct you will get a Audi Q7!!!!\n')
        user_guess = int(input('Enter your guess here:- '))

        if user_guess==random_number:
            print('***CONGRATULATION, YOU HAVE WON AUDI Q7!!!!\n')
            print('Thanks for taking part!!')
        elif user_guess>10:
            print('You have entered the number greater than 10')
        elif user_guess != random_number:
            print('Ohh, We are so sorry your guess is wrong\n')
            print(f'The number was {random_number}')
            print('Thanks for taking part!!')
        else:
            print('Please enter a valid number')

try:
    if __name__ == "__main__":
        welcome = ('''WELCOME TO SAIYAM'S LUCKY DRAW''')
        print(welcome)

        luck_draw.greeting()

        luck_draw.guess_number()

except Exception as e:
    print('Please enter a valid input')
