# Using string slicing

# def palindrome(x):
#     num_str = str(x)
#     if num_str == num_str[::-1]:
#         return True
#     else:
#         return False


# print(palindrome(-223))

#------------------------------------------------
def palindrome(x):
    temp = x
    reverse = 0
    while(x > 0):
        digit = x%10 # extract last digit from the number
        reverse = reverse*10+digit # add last digit to the reverse number
        x = x//10 # remove last digit from the number
    if reverse == temp:
        return True
    else:
        return False

print(palindrome(121))