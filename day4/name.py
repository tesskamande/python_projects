first_name= input("Enter your firstname: ")
last_name = input("Enter your lastname: ")
initials = first_name.upper()[0] + "." + last_name.upper()[0] + "."
address_name = first_name.lower() + " " + last_name.upper() 
user_name = first_name[0] + last_name.lower() 
print(initials + " ," + " " + address_name + " ," + " "  + user_name + ".")

