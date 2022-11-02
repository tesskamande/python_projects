print('Hello, welcome to my game!')
player = input("Do you want to participate! ")

if player.lower() != "yes" :
    print("Have a nice day!")

else: print("Lets play!")
score = 0
answer = input("what does CPU stand for? ")
if answer.lower() == "Central Processing Unit":
    print("correct!")
    score += 1
else: 
    print("incorrect!")

answer = input("What is the function of a router? ")
if answer.lower() == "selects a forwarding path for packets":
    print("well done!")
    score += 1
else: 
    print("incorrect!")   

print(score)