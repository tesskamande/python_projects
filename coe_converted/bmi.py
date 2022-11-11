def body_mass():
    for i  in range(1,30):
        weight = int(input("Enter your weight in kilograms: "))
        height= float(input("Enter your height in meters: "))
        BMI = weight/(height * height)
        print("your bmi is: " + str(BMI))
        if BMI < 18.5:
            print("You are underweight!")
        elif BMI >= 18.5 and BMI <= 24.9:
            print("You weight is normal")
        elif BMI >= 25 and BMI <= 29.9:
            print("You are overweight")
        else: 
            print("You are obese")   
        i += 1         
body_mass()        
