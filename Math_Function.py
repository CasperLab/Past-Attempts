#Basic Calculator
import math
from math import log10

def round_sig(x, sig):
    return round(x, sig-int(log10(abs(x)))-1)

def basic_calculator():
    
    while True:
        num1 = input("Enter first number: ")
    
        try:
            float(num1)
            num1 = float(num1)
            break
        except ValueError:
            print("Invalid number entered!")
        
    
    if num1 >= 0:
        if num1 == 0:
            print("First number is exactly 0")
        else:
            print("First number is", num1, "which is positive")           
    else:
        print("First Number is", num1, "which is negative")
      
  
    
    while True:
        num2 = input("Enter second number: ")
    
        try:
            float(num2)
            num2 = float(num2)
            break
        except ValueError:
            print("Invalid number entered!")
    
    if num2 >= 0:
        if num2 == 0:
            print("Second number is exactly 0")
        else:
            print("Second number is", num2, "which is positive")
        
    else:
        print("Second Number is", num2, "which is negative")
    
    

    while True:
        sf = input("Exact or sf?: ")
    

        if sf.lower() == "exact":
            while True:    
                op = input("Enter a mathematical operation(+,-,x,/,^): ")

                if op == "+":
                    print(num1, "+" ,num2, "=", num1 + num2)
                    break
                elif op == "-":
                    print(num1, "-" ,num2, "=", num1 - num2)
                    break
                elif op == "x":
                    print(num1, "x" ,num2, "=", num1 * num2)
                    break
                elif op == "/":
                    print(num1, "/" ,num2, "=", num1 / num2)
                    break
                elif op == "^":
                    print(num1, "^" ,num2, "=", num1 ** num2)
                    break
                else :
                    print("Invalid operation entered!")
            break 
       
        elif sf.lower() == "sf":
            while True:
                sig = input("Enter number of significant figures: ")
                try:
                    int(sig)
                    sig = int(sig)
                    break
                except ValueError:
                    print("Invalid number entered! Whole numbers only!")
            while True:    
                op = input("Enter a mathematical operation(+,-,x,/,^): ")
                num1 = int(num1)
                num2 = int(num2)

                if op == "+":
                    print(num1, "+" ,num2, "=", round_sig(int(num1 + num2), sig))
                    break
                elif op == "-":
                    print(num1, "-" ,num2, "=", round_sig(int(num1 - num2), sig))
                    break
                elif op == "x":
                    print(num1, "x" ,num2, "=", round_sig(int(num1 * num2), sig))
                    break
                elif op == "/":
                    print(num1, "/" ,num2, "=", round_sig(int(num1 / num2), sig))
                    break
                elif op == "^":
                    print(num1, "^" ,num2, "=", round_sig(int(num1 ** num2), sig))
                    break
                else :
                    print("Invalid operation entered!")
            break
        
        else:
            print("Wrong answer!")
            
    return 

def geometric_progression():
    a = float(input("First digit: "))
    r = float(input("Ratio: "))
    n = int(input("Length of progression: "))
    
    geometric = [a * r ** (n - 1) for n in range(1, n + 1)]
    
    print("Geometric Progression:", geometric)

def arithmetric_progression():
    a = float(input("First digit: "))
    d = float(input("Difference: "))
    n = int(input("Length of progression: "))
    
    arithmetric = [a + (n-1) * d for n in range(1, n + 1)]
    
    print("Arithmetric Progression:", arithmetric)

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

def choose_option():
    print("Press 1 for basic calculator\n")
    print("Press 2 to create a list of geometric progression\n")
    print("press 3 to create a list of arithmetric progression\n")
    print("Press 4 for quadratic equation solver\n")

    while True:

        option = input("Your option: ")
    
        if option == "1":
            basic_calculator()
            break
        elif option == "2":
            geometric_progression()
            break
        elif option == "3":
            arithmetric_progression()
            break
        elif option == "4":
            quadratic_eqn_solver()
            break
        else:
            print("Invalid option! Do not troll or you will be punished!")

choose_option()
