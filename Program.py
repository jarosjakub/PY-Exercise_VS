string = input("Enter a string \n")

l = len(string)
pal = ""

for i in range(l, 0, -1):
    pal = pal + string[i-1]

print(string + pal)
 