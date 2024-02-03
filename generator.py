import random
import string

length = int(input("Enter Length: "))

char = string.ascii_letters
char += string.digits
char += string.punctuation

password = ''.join([random.choice(char) for i in range(length)])

for i in range (length):
    next_character = random.choice(char)
    password += next_character

print("Your random password is:", password)
