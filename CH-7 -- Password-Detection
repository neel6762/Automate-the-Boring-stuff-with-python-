import re


def checkPassStrength(password):
    passlen = re.search(r'.{8,}', password)  # to check the length of the password
    upperCase = re.search(r'[A-Z]', password)   # Occurance of uppper case letter in the password
    lowerCase = re.search(r'[a-z]', password)   # Occurance of lower case letter in the password
    number = re.search(r'[0-9]', password)      # Occurance of a digit in the password
    spChar = re.search(r'[@#%&%*\$]', password)   # Any special Character ?
    if passlen and upperCase and lowerCase and spChar and number:
        print('Strong Password !')

    elif passlen and upperCase and lowerCase and number:
        print('Valid password, try including a special character to make it stronger !')

    else:
        print('Sorry ! thats not a good password')


def main():
    password = input('Enter your password > ')
    checkPassStrength(password)


if __name__ == '__main__':
    main()
