import random
import string

def generate_password(length, num_letters, num_numbers):
    # Ensure the length is at least 8 characters
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    
    # Ensure the sum of letters and numbers does not exceed the total length
    if num_letters + num_numbers > length:
        raise ValueError("The sum of letters and numbers cannot exceed the total password length.")
    
    # Generate random letters (both upper and lower case)
    letters = random.choices(string.ascii_letters, k=num_letters)
    
    # Generate random numbers
    numbers = random.choices(string.digits, k=num_numbers)
    
    # Generate the remaining characters (symbols)
    num_symbols = length - num_letters - num_numbers
    symbols = random.choices(string.punctuation, k=num_symbols)
    
    # Combine all the characters
    password_list = letters + numbers + symbols
    
    # Shuffle the characters to ensure randomness
    random.shuffle(password_list)
    
    # Join the list into a string to form the password
    password = ''.join(password_list)
    
    return password

# Get user input for password length, number of letters, and number of numbers
length = int(input("Enter the desired password length (minimum 8): "))
num_letters = int(input("Enter the number of letters you want in the password: "))
num_numbers = int(input("Enter the number of numbers you want in the password: "))

try:
    # Generate the password
    password = generate_password(length, num_letters, num_numbers)
    print(f"Your generated password is: {password}")
except ValueError as e:
    print(e)
