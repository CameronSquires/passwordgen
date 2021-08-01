import time
import random

alphaLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphaUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
specChars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '`', '~', '|', '/', '?', '.', ',', '>', '<', ';', ':']
password = ""

def passwordGen():
    global password
    lowerchars = int(input("Please input the amount of lowercase letters you would like. "))
    upperchars = int(input("Please input the amount of uppercase letters you would like. "))
    numchars = int(input("Please input the amount of numbers you would like. "))
    specialchars = int(input("Please input the amount of special characters you would like. "))
    while lowerchars > 0:
        password += random.choice(alphaLower)
        lowerchars -= 1
    while upperchars > 0:
        password += random.choice(alphaUpper)
        upperchars -= 1
    while numchars > 0:
        password += random.choice(nums)
        numchars -= 1
    while specialchars > 0:
        password += random.choice(specChars)
        specialchars -= 1

    passwordList = list(password)
    random.shuffle(passwordList)
    password = ''.join(passwordList)

    print(f"Your newly generated password is:\n\n{password}\n\n")

    optionMult = input("Would you like to generate another password? (Y/N)").upper()

    if optionMult == "Y":
        passwordGen()
    else:
        print("Thank you for using our program. Goodbye.")
        time.sleep(3)
        pass

passwordGen()