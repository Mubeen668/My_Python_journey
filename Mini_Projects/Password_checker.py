# user input password verification
# condition1: password should not exceed 12 characters and should not be less than 6 characters
# condition2: should not contain any spaces
# condition3: should contain at least one uppercase letter, one lowercase letter, one digit, and one special character

import re

password = input(" Enter your password:")
if len(password) < 6 or len(password) > 12:
    print("Password must be between 6 and 12 characters long.")
elif ' ' in password:
    print("Password should not contain spaces.")
elif not re.search(r"[A-Z]", password):
    print("Password must contain at least one uppercase letter.")
elif not re.search(r"[a-z]", password):
    print("Password must contain at least one lowercase letter.")
elif not re.search(r"[0-9]", password):
    print("Password must contain at least one digit.")
elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print("Password must contain at least one special character.")
else:
    print("Password is valid.")