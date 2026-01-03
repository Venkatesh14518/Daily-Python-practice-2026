# TypeError example
# len(123)
# This line is commented out because it would cause a TypeError.
# len() cannot be used on integers since integers are not collections.

# No TypeError
len("Hello")
# "Hello" is a string, which is a sequence of characters.
# len() counts how many characters are in the string (here, 5).

# Type Checking
print(type("abc"))
# Checks and prints the data type of the string "abc".
# Output will be <class 'str'>.

print(type(123))
# Checks and prints the data type of the integer 123.
# Output will be <class 'int'>.

print(type(3.14))
# Checks and prints the data type of the floating-point number 3.14.
# Output will be <class 'float'>.

print(type(True))
# Checks and prints the data type of the Boolean value True.
# Output will be <class 'bool'>.

# Type Conversion (casting functions)
str()
# Converts a value into a string (example: str(10) → "10").

int()
# Converts a value into an integer (example: int("5") → 5).

float()
# Converts a value into a floating-point number (example: float(3) → 3.0).

bool()
# Converts a value into a Boolean (example: bool(0) → False, bool(1) → True).

# User input
name_of_the_user = input("Enter your name")
# Displays the prompt "Enter your name" and waits for the user to type something.
# Whatever the user types is stored as a string in name_of_the_user.

length_of_name = len(name_of_the_user)
# Calculates the number of characters in the user's name.
# The result is an integer and is stored in length_of_name.

print(type("Number of letters in your name: "))  # str
# Checks the type of the message text.
# This confirms it is a string (str).

print(type(length_of_name))  # int
# Checks the type of length_of_name.
# This confirms it is an integer (int).

print("Number of letters in your name: " + str(length_of_name))
# Converts the integer length_of_name into a string using str().
# Then concatenates (joins) it with the message string and prints the result.
