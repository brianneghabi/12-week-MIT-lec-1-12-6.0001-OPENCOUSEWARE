import string

print("=== PASSWORD STRENGTH CHECKER ===")

password = input("Enter a password: ")

# Check for empty password
if password == "":
    print("\nPassword cannot be empty!")
else:
    points = 0
    feedback = []

    # Check length
    if len(password) < 6:
        feedback.append("Make it longer")
    elif len(password) < 8:
        points += 1
        feedback.append("Make it longer")
    elif len(password) < 12:
        points += 2
    else:
        points += 3

    # Check uppercase letters
    if any(char.isupper() for char in password):
        points += 1
    else:
        feedback.append("Add an uppercase letter")

    # Check lowercase letters
    if any(char.islower() for char in password):
        points += 1
    else:
        feedback.append("Add a lowercase letter")

    # Check numbers
    if any(char.isdigit() for char in password):
        points += 1
    else:
        feedback.append("Add a number")

    # Check special characters
    if any(char in string.punctuation for char in password):
        points += 1
    else:
        feedback.append("Add a special character")

    # Check for common/simple patterns
    common_passwords = [
        "password",
        "123456",
        "12345678",
        "qwerty",
        "abc123",
        "password123",
        "admin",
        "letmein",
        "welcome",
        "000000"
    ]

    if password.lower() in common_passwords:
        points = 0
        feedback.append("Avoid common passwords")

    # Detect simple patterns
    if password.isdigit():
        feedback.append("Avoid using only numbers")

    if password.isalpha():
        feedback.append("Add numbers and special characters")

    if len(set(password.lower())) <= 2 and len(password) >= 4:
        feedback.append("Avoid repeating the same characters")

    # Determine password strength
    if points <= 2:
        strength = "WEAK"
    elif points <= 5:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    print("\n=== RESULTS ===")
    print("Password strength:", strength)
    print("Points:", points)

    # Show feedback
    if feedback:
        print("\nHow to improve:")
        for suggestion in feedback:
            print("-", suggestion)
    else:
        print("\nGreat job! Your password meets all the requirements.")