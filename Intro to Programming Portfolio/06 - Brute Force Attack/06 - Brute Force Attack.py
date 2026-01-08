password = "12345"
attempts = 5

# A nested condition for confirming the password
while attempts > 0:
    user_input = input("Enter password: ")

    if user_input == password:
        print("Access Granted!")
        break
    else:
        attempts -= 1
        if attempts > 0: # Tracks the attempts of the user
            print(f"\nAccess Denied! You have {attempts} attempts left.")
        else:
            print("You have reached maximum attempts! Security will be alerted!")