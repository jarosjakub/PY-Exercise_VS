s = input("Enter a item name \n")
p = input("Enter a price \n")

data = s.ljust(25-len(p), ".")+p

print(data)
