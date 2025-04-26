
def has_min_length(password):
    return len(password) >= 8


def has_uppercase(password):
    for char in password:
        if char >= 'A' and char <= 'Z':
            return True
    return False


def has_lowercase(password):
    for char in password:
        if char >= 'a' and char <= 'z':
            return True
    return False


def has_digit(password):
    for char in password:
        if char >= '0' and char <= '9':
            return True
    return False


def has_special_char(password):
    special = "!@#$%^&*()_+-=[]{}|;:',.<>/?"
    for char in password:
        if char in special:
            return True
    return False


def check_password_strength(password):
    feedback = []
    passed_checks = 0

    if has_min_length(password):
        passed_checks += 1
    else:
        feedback.append("Password should be at least 8 characters.")

    if has_uppercase(password):
        passed_checks += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if has_lowercase(password):
        passed_checks += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if has_digit(password):
        passed_checks += 1
    else:
        feedback.append("Include at least one number.")

    if has_special_char(password):
        passed_checks += 1
    else:
        feedback.append("Include at least one special character (e.g. !@#$%).")

   
    if passed_checks == 5:
        strength = "Strong"
    elif passed_checks >= 4:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, feedback


def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print("\nPassword Strength:", strength)

    if feedback:
        print("Suggestions to improve:")
        for tip in feedback:
            print("-", tip)


main()
