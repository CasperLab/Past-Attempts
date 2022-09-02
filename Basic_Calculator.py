
from math import log10

def round_sig(x, sig):
    return round(x, sig-int(log10(abs(x)))-1)

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