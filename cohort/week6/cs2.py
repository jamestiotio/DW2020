def check_password(password):
    if len(password) >= 8 and password.isalnum() and sum(c.isdigit() for c in password) >= 2:
        return True

    else: return False