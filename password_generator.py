import string
import random
import sys

def generate_password(min_len=8, max_len=None):

    if max_len < min_len:
        raise ValueError("Max password length must be greater than or equal to minimum password length.")

    upper_case = string.ascii_uppercase
    lower_case = string.ascii_lowercase
    special_chars = string.punctuation
    digits = string.digits
    
    mandatory_chars = random.choice(upper_case) +  random.choice(lower_case) + random.choice(special_chars) + random.choice(digits)
    remaining_chars = upper_case + lower_case + special_chars + digits

    password_len = random.randint(min_len, max_len) - len(mandatory_chars)
    password = mandatory_chars + ''.join(random.choice(remaining_chars) for i in range(password_len))

    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password

if len(sys.argv) != 3:
    print("Please enter two arguments: [min_len] [max_len].")
    exit (1)

try:
    if int(sys.argv[1]) < 8:
        min_len = 8
    else:
        min_len = int(sys.argv[1])
    if len(sys.argv) == 3:
        max_len = int(sys.argv[2])
    else:
        max_len = 16
except ValueError:
    print("Please enter valid integer values for password lengths.")
    exit(1)

try:
    password = generate_password(min_len, max_len)
    print("Password =", password)
    print("Password length:", len(password), "\n")
except ValueError as e:
    print(e)
