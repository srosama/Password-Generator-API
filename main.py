import random
import string

def generate_password(length):
    # Define the character sets to use in the password
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    punctuation = string.punctuation
    
    # Combine the character sets into one set of all possible characters
    all_characters = uppercase_letters + lowercase_letters + digits + punctuation
    
    # Generate a random password using the defined character set
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password


password = generate_password(12)
print(password)
