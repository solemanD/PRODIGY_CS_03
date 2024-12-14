import re
def check_password_strength(password):
    """
    Assess the strength of a given password based on specific criteria.
    """
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for numbers
    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Add at least one special character (e.g., !, @, #, etc.).")

    # Determine password strength level
    if strength == 5:
        strength_level = "Strong"
    elif 3 <= strength < 5:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"

    return strength_level, feedback

def main():
   
    print("Password Strength Assessment Tool")
    print("=================================")

    password = input("Enter your password: ")
    strength_level, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength_level}")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f" - {suggestion}")

if __name__ == "__main__":
    main()
