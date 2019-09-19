import random
options = ["Rock", "Paper", "Scissors"]

computer = options[random.randint(0, 2)]

for tries in range (4): 
    player = input("Rock, Paper, or Scissors")
    if player == computer:
        print('Tie!')
    elif player == "Rock":
        if computer == "Paper":
            print('You win!')
        else:
            print('lost')
    elif player == "Paper":
        if computer == "Scissors":
            print('You lose')
        else:
            print('You win')
    elif player == "Scissors":
        if computer == "Rock":
            print('You lost')
        else:
            print('You win')
    else:
        print("That not a valid!")


# prompt user, rock paper scissors

# take the input of the user and store it into a variable

# build bot's choice: needs to choose random rock paper scissors if()
