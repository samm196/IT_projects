def validate_password(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()."

    for char in password:
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char.isdigit():
            has_digit = True
        if char in special_characters:
            has_special = True

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        print("Password is valid!")
    else:
        print("Password is invalid. Make sure it has:")
        if len(password) < 8:
            print("Must contain Atleast 8 characters")
        if not has_upper:
            print("Must contain Atleast one uppercase letter")
        if not has_lower:
            print("Must contain Atleast one lowercase letter")
        if not has_digit:
            print("Must contain Atleast one number")
        if not has_special:
            print("Must contain Atleast one special character (!@#$%^&*().)")


password = input("Enter a password: ")
validate_password(password)
            