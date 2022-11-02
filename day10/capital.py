#dictionaries - colletion of key value pairs

import random
nations = {"Kenya": "Nairobi", "Ethiopia": "Addis Ababa", "Nigeria": "Abuja", "South Africa": "Cape Town"}

def country_list():
    country = []
    for countries in nations:
        country.append(countries)
    return(country) 

new_list = country_list()
selected_country = random.choice(new_list)      
capital_value = nations.get(selected_country)

for x in range(1,100):
    capital= input("what is the capital city of " + selected_country + " " ) 
    if capital.lower() != capital_value.lower():
        x += 1
        print("You have entered the wrong capital city!")
    else:
        print("Well done! You are correct" )
        print("This took you ", x, "trials" )
        break
        

