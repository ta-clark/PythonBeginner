# Define password check. Ask for user input.

def password_checker():
    password = input("Enter a password that is at least 7 characters, no more than 21 characters, does not contain umgc and contains # so long as # is not the first or last character: ")

# Password must contain at least 7 characters and no more than 21 characters
    if len(password) > 7 and len(password) < 21: 
        print("Pass: Password length")
    else:
        return print("Fail: Password length.")
    if "umgc" not in password.lower(): # Password cannot contain "umgc"
        print('Pass: Password does not contain "umgc"')
    else:
        return print('Fail: Password contains "umgc"')
    if "#" in password[1:-1]: # "#" Cannot be the first or last character
        print('Pass: Password contains "#"') #Password must contain "#"
    else:
        return print('Fail: Password does not contain "#"')
    print("Great job! Password is secure.") # Display pass result
    
password_checker()

