def main():
    mortages = int(input("enter your mortages: "))
    auto_mobile = int(input("enter your auto_mobile loan: "))
    credit_card = int(input("enter your credit card loan: "))
    income = int(input("enter your monthly income: "))
    debts = mortages + auto_mobile + credit_card

    debt_ratio = (debts)/ income

    if income < debt_ratio:
        print("You qualify for a loan!")
    else:
        print("You don't qualify for a loan!")    

main()        
