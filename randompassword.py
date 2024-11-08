import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if use_uppercase else ''
    numbers = string.digits if use_numbers else ''
    symbols = string.punctuation if use_symbols else ''
    
    # Combine all selected character sets
    all_characters = lowercase + uppercase + numbers + symbols

    # Ensure at least one character type is selected
    if not all_characters:
        raise ValueError("At least one character type must be selected.")

    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    # Get user input
    length = int(input("Enter the desired password length: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    # Generate and display the password
    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
