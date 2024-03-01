import re
email = input("Write your email ").strip()

if re.search(".+@.+", email):
    print("valid")
else:
    print("invalid")