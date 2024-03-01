# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         # except Exception as e: # bad pratice
#         except ValueError: # good pratice
#             print("x is not integer")
#         else:
#             break
#     print(f"x is {x}")

# if __name__ == '__main__':
#     get_int()


def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("x is not an integer")
        else:
            return x

main()
