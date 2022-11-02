phone = input("enter your phone number: ")
def phone_number(phone):
        Num = phone.split("-")
        Area_code = Num[0]
        Num_end = Num[1:]
        number = ""
        for n in Num_end:
            for i in range(len(n)):
                if n[i] in 'ABC':
                    number = number + '2'
                elif n[i] in 'DEF':
                    number = number + '3'
                elif n[i] in 'GHI':
                    number = number + '4'
                elif n[i] in 'JKL':
                    number = number + '5'
                elif n[i] in 'MNO':
                    number = number + '6'
                elif n[i] in 'QRS':
                    number = number + '7'
                elif n[i] in 'TUV':
                    number = number + '8'
                elif n[i] in 'WXY':
                    number = number + '9'        
            number = number+'-'
        return Area_code+'-'+number[:-1]    

translated = phone_number(phone)        
print(translated)