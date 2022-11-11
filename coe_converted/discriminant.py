import math
def equations():
    i = 0
    while i < 20:
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))
        c = float(input("Enter the value of c: "))
        discri = (b * b) - (4 * a * c)
        discr_sqr = math.sqrt(abs(discri))

        if discri > 0:
            print("The roots are real")
            print((-b + discr_sqr)/ (2 * a))
            print((-b - discr_sqr)/ (2 * a))
        elif discri == 0:
            print("The roots are equal")    
            print((-b + discr_sqr)/ (2 * a))
            print((-b - discr_sqr)/ (2 * a))
        else:
            print("The roots are complex")
            print((-b + discr_sqr)/ (2 * a))
            print((-b - discr_sqr)/ (2 * a))  
            
        i +=1    
    

equations()
