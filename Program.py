num = int(input("Enter a number \n"))

num_orig = str(num)
num_temp = num
suma = 0
suma_temp = 0
reverse = ""
while num_temp > 0:
    num_temp = num // 10
    suma_temp = num % 10
    reverse = reverse + str(suma_temp)
    num = num - suma_temp
    suma = suma + suma_temp
    num = int(num / 10)

if num_orig == reverse:
    print ("Number is a palindrome")
else:
    print ("Number is not a palindrome")

    