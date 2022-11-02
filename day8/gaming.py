import random

def game():
    tie = True
    while tie:
        num = random.randint(1,3)
        computer = ""
        if num == 1:
            computer = "rock"
        if num == 2:
            computer ="paper"
        if num ==3:
            computer = "scissors"

        player= input("Enter rock, paper or scissors: ") 
        print("computer played", computer, "\n")  

        if computer == player:
            print("it's a tie\n")    
            num = random.randint(1,3)
        if computer == "rock" and player == "paper":
            print("you win")
            tie = False
        if computer == "paper" and player == "rock":
            print("you lose")
            tie = False        
        if computer == "paper" and player == "scissors":
            print("you win")
            tie = False       
        if computer == "scissors" and player == "paper":
            print("you lose")
            tie = False      
        if computer == "rock" and player == "scissors":
            print("you lose")
            tie = False              
        if computer == "scissors" and player == "rock":
            print("you win")
            tie = False     
game()                
