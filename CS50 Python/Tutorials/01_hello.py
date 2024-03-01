# Ask user's for their name
name = input("What's your name? ").strip().title()
# print("Hello", name)

# Remove white spaces and capitilize user's name 
# name = name.strip().title()

# split user's name into first name and last name
first, last = name.split(" ")




# Escape character, we can use the "" '' in string using escape character
# print("Hello, \'Friend\'")

# Capitilize the user's name
# name = name.capitalize() # capitilize only first letter

# name = name.title() # convert into title case -> Ajay Kumar

# format string (f'') 
print(f"Hello, {first} ")