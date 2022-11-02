message =""
vegetarian_person = input("Is anyone in the party vegetarian? ") .lower()

if vegetarian_person == "yes" or vegetarian_person == "no":
    vegan_person = input("Is anyone in the party vegan? ") .lower()
    if vegan_person == "yes" or vegan_person == "no":
        gluten_person = input("Is anyone in the party gluten-free? ") .lower()
        if gluten_person == 'yes' or gluten_person =='no':
            message = "Here are your restaurant choices:\n"
            if vegetarian_person=='yes':
                if vegan_person=='yes':
                    if gluten_person == 'yes' or gluten_person =='no':
                        message += "corner cafe\n" + "The chief's Kitchen\n"
                else:
                    if gluten_person == 'yes':
                        message += "Main street pizza company\n" + "corner cafe\n" + "The chief's kitchen\n"
                    else:
                        message += "Main street pizza company\n" + "corner cafe\n" + "The chief's kitchen\n" + "mama's fine italian\n"
            else:
                if vegan_person =='yes':

                    if gluten_person == 'yes' or gluten_person =='no':
                        message += "corner cafe\n" + "The chief's kitchen\n" 
                else:
                    if gluten_person == 'yes':
                        message += "Main street pizza company\n" + "corner cafe\n" + "The chief's kitchen\n"
                    else:
                        message += "joe's gourmet burgers\n" + "Main street pizza company\n" + "corner cafe\n" + "The chief's kitchen\n" + "mama's fine italian\n"
        else:
            message= "Enter either 'yes' or 'no'."
    else:
         message= "Enter either 'yes' or 'no'."
else:
    message= "Enter either 'yes' or 'no'."

print(message)           