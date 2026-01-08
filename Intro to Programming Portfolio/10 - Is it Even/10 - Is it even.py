# Function to tell if it a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(f"\n{number} is an even number.")
    else:
        print(f"\n{number} is an odd number")

# Activates the main function
def main():
    try:
        user_num = int(input("Enter a number: "))
        result = check_even_odd(user_num)
        print(result)
    except ValueError:
        print("Please enter a valid integer")

if __name__ == "__main__":
    # Calls the main function
    main()