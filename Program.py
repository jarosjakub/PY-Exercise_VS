number = int(input("Enter a number \n"))

fact = number
for i in range(number-1, 0, -1):
    fact = fact * i

print("Factorial of", number, "is", fact)