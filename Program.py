number = int(input("How many numbers will you enter? \n"))
count = 0
num_max = 0

while count < num_of_num:
    num = int(input("Enter a number \n"))
    count += 1
    if num > num_max:
        num_max = num

print("The biggest number is ", num_max)