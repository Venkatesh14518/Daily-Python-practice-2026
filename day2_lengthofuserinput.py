name = "Jack"          # Assigns the string "Jack" to the variable name
print(name)            # Prints the current value stored in name

name = "Angela"        # Reassigns the variable name to a new value "Angela"
print(name)            # Prints the updated value of name

print(len(name))       # Calculates and prints the number of characters in "Angela"

# print(len(input("what is your name?")))
# This commented line would:
# 1. Ask the user for their name
# 2. Immediately calculate the length of the input
# 3. Print the length
# It is commented out, so Python ignores it

username = input("What is your name?")  # Takes input from the user and stores it in username
length = len(username)                  # Calculates the number of characters in username
print(length)                            # Prints the length of the username
