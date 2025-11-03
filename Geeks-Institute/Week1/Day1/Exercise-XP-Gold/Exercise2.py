month = int(input("Enter a month (1-12): "))

if month in [3, 4, 5]:
    print("It's Spring")
elif month in [6, 7, 8]:
    print("It's Summer")
elif month in [9, 10, 11]:
    print("It's Autumn")
elif month in [12, 1, 2]:
    print("It's Winter")
else:
    print("Invalid month! Please enter a number from 1 to 12.")
