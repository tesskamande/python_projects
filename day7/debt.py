hours_slept = int(input("what is the number hours you sleep each day? " + "Monday: "))
tue=int(input("Tuesday: "))
wed=int(input("Wednesday: "))
thu=int(input("Thursday: "))
fri=int(input("Friday: "))
sat=int(input("Saturday: "))
sun=int(input("Sunday: "))

desired_hours=(8*7)
hours = (hours_slept+tue+wed+thu+fri+sat+sun)

print("you have an avearage of " + str(hours)+ " hours of sleep")
if hours<desired_hours:
    print("you have a sleep debt")
else:
    print("Nice sleeping schedule")    