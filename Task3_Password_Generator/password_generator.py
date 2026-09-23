import random
import string

print("===== PASSWORD GENERATOR =====")

try:
    length = int(input("Enter the password length: "))

    if length < 4:
        print("Password length should be at least 4. ")
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))

        print ("Generated Password: ", password)

except ValueError:
    print("Please enter a valid number. ")
