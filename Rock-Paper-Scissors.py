import random

print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissor wins \n")
    

def rps():
    
    choices = ['rock', 'paper', 'scissors']
    user = input("Enter your choice (rock, paper, scissors): ").lower()
    computer = random.choice(choices)

    if user not in choices:
        print("Invalid input")
        return
    
    print(f"Computer choice: {computer.upper()}")
    print(f"User choice: {user.upper()}")

    if user == computer:
        print("It's a tie!!")
    else:
        if (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
            print("You win!!")
        else:
            print("You lose!!")

while True:
    rps()
    print("Do you want to play again?")
    play_again = input("Enter 'y' for yes or 'n' for no: ").lower()
    if play_again == 'n':
        break
