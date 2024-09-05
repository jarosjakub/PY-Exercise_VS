number = int(input("Enter number of terms \n"))
print("---------------")

fib1 = 0
fib2 = 1
fib = 0

print(fib1)
print(fib2)

for i in range(0, number-2):
    fib = fib1 + fib2
    print (fib)
    fib1 = fib2
    fib2 = fib

