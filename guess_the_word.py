import random
import datetime
class Welcome:
    # This greeting function will greet the user according to the time and take input
    @staticmethod
    def greeting():
        print('''WELCOME TO SAIYAM'S GAME ZONE
        1. Enter 1 to start the game
        2. Enter 2 to exit the game''')
        choice = int(input('Enter your choice here:- '))
        if choice==1:
            pass
        elif choice==2:
            exit()

        name = input('Enter your name here:- ')
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            print(f'Good Morning {name}')
        elif hour>=12 and hour<17:
            print(f'Good Afternoon {name}')
        else:
            print(f'Good Evening {name}')

class game(Welcome):

    @staticmethod
    def start_game():
        
        list_of_words = ['hello', 'python', 'laptop', 'phone', 'computer', 'keyboard', 'mouse']
        random_number= random.randint(1,7)
        random_word = None
        if random_number==1:
            random_word = 'hello'
        elif random_number==2:
            random_word = 'python'
        elif random_number==3:
            random_word = 'laptop'
        elif random_number==4:
            random_word = 'phone'
        elif random_number==5:
            random_word = 'computer'
        elif random_number==6:
            random_word = 'keyboard'
        else:
            random_word = 'mouse'

        guessed_word = input('Enter your guess:- ') 
        if guessed_word != random_word:
            print(f'{guessed_word} is the wrong guess...Try again')

        elif guessed_word==random_word:
            print(f'You guessed the word right....Well done!!')
            print('Thanks for playing this game')
            exit()
try:
    if __name__ == "__main__":
        Welcome.greeting()

        while True:
            game.start_game()

except Exception as e:
    print('Please enter a valid input.')
