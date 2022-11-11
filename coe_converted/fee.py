def school_fees():
    hours = int(input("Enter the number of hours of study: "))
    if hours > 15:
        cost = hours * 445
        print("your total cost is ksh " + str(cost))
    else:
        cost = hours * 500 
        print("Your total cost is ksh " + str(cost))

school_fees()           