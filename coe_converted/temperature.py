def temp():
    for i in range (1,10):
        temperatures = float(input("Enter the temperature in fahrenheit: "))
        celcius = (temperatures - 32)/(1.8)
        print("The temperature in celcius is: " + str(celcius))
        i +=1
temp()
