import random
choices = ("rock", "paper", "scissors")

computer = random.choice(choices)

player = choices
trials = 0
while player not in choices:
    player = input("What is your choice? ")
    if player == computer:
        print("player: ", player)  
        print("computer: ", computer) 
        print("it's a tie!")  
        trials += 1
    elif player == "rock":
        if computer == "paper":
            print("player: ", player)
            print("computer: ", computer)
            print("you lose!")   
        if computer == "scissors":
            print("player: ", player)
            print("computer: ", computer)
            print("you win!") 
    elif player == "paper":
        if computer == "rock":
            print("player: ", player)
            print("computer: ", computer)
            print("you win!")   
        if computer == "scissors":
            print("player: ", player)
            print("computer: ", computer)
            print("you lose!")
    elif player == "scissors":
        
        if computer == "paper":
            print("player: ", player)
            print("computer: ", computer)
            print("you win!")   
        if computer == "rock":
            print("player: ", player)
            print("computer: ", computer)
            print("you lose!")   
    else: 
        print("invalid choice!")                               

