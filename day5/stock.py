stock = 2000
share = 40.00
broker= (2000*40.00)*0.03
money_paid= (2000*40.00)
print("The money used to buy the stock: " + str(money_paid))
print("The money paid to broker during buying: " +str(broker))

#selling
stock1 = 2000
share1= 42.75
broker1= (2000*42.75)*0.03
selling_price =(2000*42.75)
print("selling price is: " + str(selling_price))
print("The broker was paid: " + str(broker1))

average_selling=(selling_price - (broker + broker1))
print(average_selling)
if average_selling < selling_price:
    print("He made a loss")
else:
    print("He made a profit")    