def get_binary():
    try:
        x = input("What's x? ")
        x = x.encode('ascii')[0]
        print("x is not integer, im converting this string to binary")
        # print(f"x is {x}")
    except Exception as e :
        print(f"Error: {e}")
    return x

print("x: ",get_binary())