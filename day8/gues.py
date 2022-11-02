import random
def guessing():
    num = random.randint(1,100)
    guess = 0
    count = 0
    while guess != num:
        guess = int(input("Guess the number: "))
        count += 1
        if guess < num:
            print("Too low, try again")
        if guess == num:
            print("Congratualations! its correct")
            print("thats took you", count, "guesses\n")
            print("generating a new number...\n")
            num = random.randint(1,100)
            guess = 0
            count = 0
        if guess> num:
            print("Too high try again")
            
guessing()                