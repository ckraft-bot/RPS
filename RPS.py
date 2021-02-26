import random

while True:
        print('Make your choice:')
        choice = str(input())
        choice = choice.lower()

        print("My choice is", choice)

        choices = ['rock', 'paper', 'scissors']

        computer_choice = random.choice(choices)

        print("Computer choice is", computer_choice)
        if choice in choices: 
            if choice == computer_choice:
                    print('it is a tie')
            if choice == 'rock':
                if computer_choice =='paper':
                    print('You lose, sorry. :(')
                elif computer_choice =='scissors':
                    print('You win, Congrats! :)')
            if choice == 'paper':
                if computer_choice =='scissors':
                    print('You lose, sorry. :(')
                elif computer_choice =='rock':
                    print('You win, Congrats! :)')
            if choice == 'scissors':
                if computer_choice == 'rock':
                    print('you lose, sorry:(')
                elif computer_choice == 'paper':
                    print ('You win, Congrats! :)')
else:
        print('invalid choice, try again')

        print()