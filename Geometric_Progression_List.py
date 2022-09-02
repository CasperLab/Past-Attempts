a = float(input("First digit: "))
r = float(input("Ratio: "))
n = int(input("Length of progression: "))

# nth term of GP = ar^(n-1)

geometric = [a * r ** (n - 1) for n in range(1, n + 1)]
#This creates a list

print("Geometric Progression:", geometric)
 