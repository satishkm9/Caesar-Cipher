import re

def check_password_strength(password):
    """Assess the strength of a given password and provide feedback."""
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[@$!%*?&#]', password))

    strength = 0
    criteria_met = 0

    if length_criteria:
        strength += 1
        criteria_met += 1
    if uppercase_criteria:
        strength += 1
        criteria_met += 1
    if lowercase_criteria:
        strength += 1
        criteria_met += 1
    if number_criteria:
        strength += 1
        criteria_met += 1
    if special_char_criteria:
        strength += 1
        criteria_met += 1

    feedback = []

    if criteria_met == 5:
        feedback.append("Password is very strong.")
    elif criteria_met == 4:
        feedback.append("Password is strong.")
    elif criteria_met == 3:
        feedback.append("Password is medium.")
    else:
        feedback.append("Password is weak.")
    
    if not length_criteria:
        feedback.append("Password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Password should include at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Password should include at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Password should include at least one number.")
    if not special_char_criteria:
        feedback.append("Password should include at least one special character (@$!%*?&#).")

    return "\n".join(feedback)

def main():
    print("Password Complexity Checker")
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()
