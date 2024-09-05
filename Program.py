enter = float(input("Enter a decimal number \n"))
number = int(enter)
num = number
temp = ""
bin_number = ""

while num != 0:
    temp = str(num % 2) 
    num = int(num / 2)
    bin_number = temp + bin_number

print(enter, "in binary is", bin_number)
