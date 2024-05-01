# import random
# import string

# def generatePassword(minLength, numbers=True, specialCharacters=True):
#     letters = string.ascii_letters
#     digits = string.digits
#     special = string.punctuation

    
#     characters = letters
#     if numbers:
#         characters += digits
#     if specialCharacters:
#         characters += special

#         pwd = ""
#         meetsCriteria = False
#         hasNumber = False
#         hasSpecial = False

#         while not meetsCriteria or len(pwd) < minLength:
#             newChar = random.choice(characters)
#             pwd += newChar

#             if newChar in digits:
#                 hasNumber = True
#             elif newChar in special:
#                 hasSpecial = True

#             meetsCriteria = True
#             if numbers:
#                 meetsCriteria = hasNumber
#             if specialCharacters:
#                 meetsCriteria = meetsCriteria and hasSpecial
        
#         return pwd

# minLength = int(input("Enter the minimum length: "))
# hasNumber = input("Do you want to have numbers (y/n)? ").lower() == "y"
# hasSpecial = input("Do you want to have special characters (y/n)? ").lower() == "y"
# pwd = generatePassword(minLength, hasNumber, hasSpecial)
# print(f"The generated password is: {pwd}")
import random
import string

def generatePassword(minLength, numbers=True, specialCharacters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if specialCharacters:
        characters += special

    pwd = ""
    meetsCriteria = False
    hasNumber = False
    hasSpecial = False

    while not meetsCriteria or len(pwd) < minLength:
        newChar = random.choice(characters)
        pwd += newChar

        if newChar in digits:
            hasNumber = True
        elif newChar in special:
            hasSpecial = True

        # Check if all criteria are met before setting meetsCriteria to True
        meetsCriteria = True
        if numbers:
            meetsCriteria = hasNumber
        if specialCharacters:
            meetsCriteria = meetsCriteria and hasSpecial

    return pwd

minLength = int(input("Enter the minimum length: "))
hasNumber = input("Do you want to have numbers (y/n)? ").lower() == "y"
hasSpecial = input("Do you want to have special characters (y/n)? ").lower() == "y"
pwd = generatePassword(minLength, hasNumber, hasSpecial)
print(f"The generated password is: {pwd}")

