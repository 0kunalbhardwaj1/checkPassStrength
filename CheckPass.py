import string
import getpass

def checkPass():
    password = getpass.getpass("Please enter your password: ")
    passStrength = 0
    remarks = ''
    lower_count = upper_count = num_count = space_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            space_count += 1
        else:
            special_count += 1

    if lower_count >=1:
        passStrength += 1
    if upper_count >=1:
        passStrength += 1
    if num_count >=1:
        passStrength += 1
    if space_count >=1:
        passStrength += 1
    if special_count >=1:
        passStrength += 1
    
    if passStrength == 1:
        remarks = 'Very Weak Password!'
    elif passStrength == 2:
        remarks = 'Weak Password'
    elif passStrength == 3:
        remarks = 'Improvable Password'
    elif passStrength == 4:
        remarks = 'Good Password'
    elif passStrength == 5:
        remarks = 'Strong Password'
    
    print("Password Strength:",passStrength)
    print("Hint: ",remarks)

def askPass(newPass=False):
    valid = False
    if newPass:
        prompt = 'Do you want to enter another pwd (y/n): '
    else:
        prompt = 'Do you want to check pwd (y/n): '

    while not valid:
        choice = input(prompt)
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid, Try Again')

if __name__ == '__main__':
    print('+++ welcome to PWD checker +++')
    while True:
        if not askPass():
            break
        checkPass()
        if not askPass(True):
            break