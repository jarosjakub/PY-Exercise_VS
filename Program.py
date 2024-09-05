number = int(input("Enter a number \n"))

prime = 0
for i in range(2, number):
    if number % i == 0:
        prime += 1

if prime == 0:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")

