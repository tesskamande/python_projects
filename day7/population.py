desirable = 56
total_sleep = 0
for x in range(1,8):
    print("day: " , x)
    actual_sleep = int(input("enter the amount of sleep: "))
    total_sleep += actual_sleep
if total_sleep < desirable:
        print("you do not have sleep debt")
else: 
        print("you have a sleep debt")    