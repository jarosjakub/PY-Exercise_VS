#---------------------------------------- Counting the number of digits in a number
# num = int(input("Enter a number \n"))

# num_temp = num
# count = 0
# i = 10
# while num_temp > 0:
#     num_temp = num // i
#     count += 1
#     i = i * 10

# print ("The number has ", count, " digits")

#---------------------------------------- Find sum of digits in a number
# num = int(input("Enter a number \n"))

# num_temp = num
# suma = 0
# suma_temp = 0
# while num_temp > 0:
#     num_temp = num // 10
#     suma_temp = num % 10
#     num = num - suma_temp
#     suma = suma + suma_temp
#     num = int(num / 10)

# print("The sum of digits is ", suma)

#---------------------------------------- Reversing a number
# num = int(input("Enter a number \n"))

# num_temp = num
# suma = 0
# suma_temp = 0
# reverse = ""
# while num_temp > 0:
#     num_temp = num // 10
#     suma_temp = num % 10
#     reverse = reverse + str(suma_temp)
#     num = num - suma_temp
#     suma = suma + suma_temp
#     num = int(num / 10)

# print(reverse)

#---------------------------------------- Check if number is a palindrome
# num = int(input("Enter a number \n"))

# num_orig = str(num)
# num_temp = num
# suma = 0
# suma_temp = 0
# reverse = ""
# while num_temp > 0:
#     num_temp = num // 10
#     suma_temp = num % 10
#     reverse = reverse + str(suma_temp)
#     num = num - suma_temp
#     suma = suma + suma_temp
#     num = int(num / 10)

# if num_orig == reverse:
#     print ("Number is a palindrome")
# else:
#     print ("Number is not a palindrome")

