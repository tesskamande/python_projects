import random

def main():
    guess= int(input("enter the range of numbers: "))
    file = open("number.txt", "w")
    for i in range(guess):
        num = random.randrange(1,500)
        num= str(num)
        file.write(num)
    file.close()
    file = open("number.txt", "r")
    print(file.read())
main()