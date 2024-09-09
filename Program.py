pass1 = input("Enter a passwrod \n")
pass2 = input("Confirm your password \n")

if pass1 == pass2:
    print("Password ok")
elif pass1.casefold() == pass2.casefold():
    print("Passwords are not the same; check your cases")
else:
    print("Passwords are not the same")

