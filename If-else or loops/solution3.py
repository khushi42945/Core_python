# 3.Password Criteria Validator
# Problem Statement:
# Write a validation script to check if a user's input password meets the minimum security requirements:
# Minimum length of at least 8 characters.
# Contains at least one numeric digit (0-9).
# Contains at least one special character (e.g., @, #, $, %, !, &, *).

password = input("enter your password")


special_chars = "@#$%!&*^_+="
hd =False
hs =False

for char in password:
    if char.isdigit():
        hd = True
    elif char in special_chars:
        hs = True


if len(password) < 8:
    print("Invalid: Password must be at least 8 characters long.")
elif not hd:
    print("Invalid: Password must contain at least one numeric digit (0-9).")
elif not hs:
    print("Invalid: Password must contain at least one special character (@, #, $, %, !, &, *).")
else:
    print("Valid Password! Your password is secure.")