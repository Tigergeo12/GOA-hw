print("1. enter miles to convert to km ")
print("2. enter km to convert to miles")
choice = int(input("enter 1 or 2"))
num = int(input("number you want to conver"))
if choice == 1:
    print(num * 0.6) 
elif choice ==2:
    print(num * 1.6)
else:
    print("invalid input ")