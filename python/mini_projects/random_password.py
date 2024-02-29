import random
import string

collection_str = string.ascii_letters + string.punctuation + string.hexdigits

length = int(input("Enter the length of password: "))

password = ""

# for _ in collection_str:
#     if len(password) <= length:
#         password += random.choice(collection_str)

# -------------------------------------------------------------------------------

# Another method
password = ''.join(random.choice(collection_str) for _ in range(length) if len(password) <= length)

print("Your Password: ",password) 