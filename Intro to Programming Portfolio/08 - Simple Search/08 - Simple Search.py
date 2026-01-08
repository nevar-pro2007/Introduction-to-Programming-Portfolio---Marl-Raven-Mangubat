names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"] # Dictionary for names
search = input("Who are you looking for?: ") # User input for searching name

if search in names: # To confirm if the name was found
    print(f"{search} is in the list.")
else:
    print(f"{search} is not here.")