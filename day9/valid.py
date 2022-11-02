def main():
    num = input("enter your 20 numbers separated by space: ")
    number = num.split()
    print("list: ", number)
    if len(number) != (20):
        print("number is too low")
    else: print("number is too high")       
    for i in range(len(number)):
        number[i] = int(number[i])    
    print("The sum is: ", sum(number))    
    print("The highest number is: ", max(number))    
    print("The lowest number is: ", min(number))    
    average_number = (sum(number))/(len(number))
    print("The average is: ", average_number)
main()