"""
This program is a simple password generator
"""

from random import choices
import string
import time

filename = 'generated_password.txt'

def current_time():
    """Returns the current state of the day"""

    current_time = time.localtime()
    
    if current_time.tm_hour < 12:
        return "Good morning!"
    elif 17 > current_time.tm_hour  > 12:
        return "Good afternoon!"
    else:
        return "Good evening!"


def generate_password():
    """Generates a random 10 character length password"""

    # List of letters and digits from which the application will draw password
    alphabet = string.ascii_letters
    password_selection = list(alphabet)
    password_selection += 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

    # From password_selection, we take 10 random characters, and we return it
    generator = choices(password_selection, k=10)
    generated = ''.join(map(str, generator))
    generated = generated.strip()
    return generated


def ask_user():
    """Asks a user for input referring to the questions given"""

    print("\nHello and " + current_time())
    select = input(
    """
    Would you like to open or create a new password?
    Enter 'quit' to exit the program
    Type 'create' to generate a password 
    Type 'open' to open an existing password
    ~~~ """
    ) 
    return select


def open_file():
    """Checks if the user info is stored"""

    with open(filename, 'r') as f:
        name = input("What is your name? ")
        name = name.title()

        if name.lower() == 'quit':
            raise SystemExit

        for line in f:
            if name in line:
                print(f"\nHello {name}, this is your password:")
                print(line.strip())
                break

        else:
            print("Unable to find your information")


def create_profile():
    """Creates a user profile with the desired password"""

    name = input("\nWhat is your name? ")
    if name.lower() == 'quit':
        raise SystemExit

    description = input("Enter a description: ")
    if description.lower() == 'quit':
        raise SystemExit
    
    print("Here is your password: " + generate_password())
    confirm_password = input("Do you like this password? ")

    if confirm_password.lower() == 'yes':
        with open(filename, 'a') as f:
            user_profile = f"{name.title()} | {description.title()} | {generate_password()}"
            f.write(user_profile + "\n")
            print("Your password is now stored!")

    elif confirm_password.lower() == 'no':
        print("Reinitiating the program")

    elif confirm_password.lower() == 'quit':
        raise SystemExit
        
    else:
        print("Only Yes/No answer is accepted")


if __name__ == '__main__':
    try:
        while True:
            answer = ask_user()

            if answer == 'open':
                open_file()
            elif answer == 'create':
                create_profile()
            elif answer == 'quit':
                break
            else:
                print("Invalid input")

    except KeyboardInterrupt:
        print("\nPlease refrain from entering unnecessary keyboard commands")