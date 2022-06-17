print("Welcome to Rock, Paper, Scissors. [RPS]")
import random
choices = ['rock', 'paper', 'scissors']
while True:
    while True:
        print("Make your choice\n'Rock', 'Paper', or 'Scissors'")
        human_opt = input("Press 'r' for rock, 'p' for paper, or 's' for scissors: ")
        human_option = human_opt.lower()
        human_choice = ["rock", "paper", "scissors"]
        if human_option == "r":
            human_choice = "rock"
            break
        elif human_option == "p":
            human_choice = "paper"
            break
        elif human_option == "s":
            human_choice = "scissors"
            break
        else:
            print("Invalid choice\n Make sure you press only one key:\n 'r' for rock, 'p' for paper, or 's' for scissors.\n    P.S - Press 'Ctrl' + P to exit program\n    Press Enter to continue")
            input("Press enter to start again")
    computer_choice = random.choice(choices)
    print(f"\nPlayer ({human_choice}) : CPU ({computer_choice})")
    input("Press enter to see result")
    if human_choice == computer_choice:
        print("The computer can read your mind. It's a tie! Try agian")
        input("Press enter to try again")
    else:
        break

if human_choice == "rock":
    if computer_choice == "scissors":
        print("rock DESTROYS scissors!!! You rock!")
    else:
        print("Awwwww. Paper covers rock.\n You lose")
elif human_choice == "paper":
    if computer_choice == "rock":
        print("paper SWALLOWS rock!!! You win!")
    else:
        print("Awwwww. Scissors cuts paper.\n You lose")
elif human_choice == "scissors":
    if computer_choice == "paper":
        print("scissors SHREDS paper!!! You win!")
    else:
        print("Awwwww. Rock smashes your scissors.\n You lose")
print("Thank you for testing our product and believing in us!\n Goodbye...")