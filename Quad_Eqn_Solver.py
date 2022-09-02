import math

# (-b +- sqrt(b^2 - 4 * a * c))/2 * a

def quadratic_eqn_solver():
    print("In the form of ax^2 + bx + c = 0, enter values of a, b, c")

    while True:
         a = input("a: ")         
         try:
             float(a)
             a = float(a)
             break
         except ValueError:
             print("Invalid value for a entered!")
    while True:
         b = input("b: ")         
         try:
             float(a)
             b = float(b)
             break
         except ValueError:
             print("Invalid value for b entered!")
    while True:
         c = input("c: ")         
         try:
             float(c)
             c = float(c)
             break
         except ValueError:
             print("Invalid value for c entered!")        
    
    
    if (b ** 2 - 4 * a * c) < 0:
        print("Your equation is:",a,"x^2 +", b,"x +",c,"= 0")
        print("No Real Solution!")
    elif a == 0:
        if a == 0 and b != 0:
            print("Your equation is:",b,"x +",c,"= 0")
            x_s = -c/b
            print("x =", x_s)
        else:
            print("What's the point of this?")
    else:    
        print("Your equation is:",a,"x^2 +", b,"x +",c,"= 0")
        x_1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x_2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        if x_1 != x_2:
            print("x1 =", x_1)
            print("x2 =", x_2)
            print("There is 2 real solutions!")
        else:
            print("x1 = x2 =", x_1)
            print("There is 1 real solution!")

quadratic_eqn_solver()
