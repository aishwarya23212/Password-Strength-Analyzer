## Password Strength Analyzer
import re

# Optional: List of common passwords
common_passwords = ["123456", "password", "123456789", "qwerty", "abc123"]

# Step 1: Get password from user
password = input("Enter your password: ")

# Step 2: Initialize score
score = 0

# Step 3: Check length
if len(password) >= 12:
    score += 1

# Step 4: Check uppercase letters
if re.search("[A-Z]", password):
    score += 1

# Step 5: Check lowercase letters
if re.search("[a-z]", password):
    score += 1

# Step 6: Check numbers
if re.search("[0-9]", password):
    score += 1

# Step 7: Check special characters
if re.search("[@#$%!&*]", password):
    score += 1

# Step 8: Check if password is common
if password.lower() in common_passwords:
    print("\nWarning: This password is very common. Choose a stronger one!")

# Step 9: Determine strength
if score <= 2:
    strength = "Weak"
elif score <= 4:
    strength = "Medium"
else:
    strength = "Strong"

# Step 10: Show results
print("\nPassword Strength:", strength)
print("Score:", score, "/5")

# Step 11: Give suggestions for improvement
if strength == "Weak":
    print("Suggestions to improve:")
    print("- Use at least 8 characters")
    print("- Include uppercase letters")
    print("- Include lowercase letters")
    print("- Include numbers")
    print("- Include special symbols like @, #, $, !, &")
elif strength == "Medium":
    print("Suggestions to improve further:")
    print("- Add more characters")
    print("- Include more symbols and numbers")
