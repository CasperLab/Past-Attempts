a = float(input("First digit: "))
d = float(input("Difference: "))
n = int(input("Length of progression: "))

# nth term of AP = a+(n-1)d

arithmetric = [a + (n-1) * d for n in range(1, n + 1)]

print("Arithmetric Progression:", arithmetric)
