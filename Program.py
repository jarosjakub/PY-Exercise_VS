amount = int(input("Enter the order amount \n"))

if amount <= 1000:
    print("Your discount is 10 %")
elif amount > 1000 and amount <= 5000:
    print("Your discount is 20 %")
elif amount > 5000 and amount <= 10000:
    print("Your discount is 30 %")
else:
    print("Your discount is 50 %")

