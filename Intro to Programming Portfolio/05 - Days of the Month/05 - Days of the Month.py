# Dictionary of month numbers and days
month_days = {
    1: 31, 2:28, 3:31, 4:30, 5:31, 6:30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

month = int(input("Enter the month (1-12): "))

if month in month_days: # A nested condition to confirm if it is leap year
    if month == 2:
        leap = input("Is this a leap year? Yes or No?: ")
        if leap == "Yes":
            print("There are 29 days.")
        else:
            print("There are only 28 days.")
    else:
        print(f"There are {month_days[month]} days.") 
else:
    print("The number is invalid.")