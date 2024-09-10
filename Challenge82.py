#---------------------------------------- Find user id and domain name from email adress
cnum = input("Enter your email \n")

split = cnum.split("@")

print("The user id is:", split[0])
print("The domain name is:", split[1])


