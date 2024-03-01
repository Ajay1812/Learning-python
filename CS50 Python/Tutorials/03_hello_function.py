# def hello(to="World!"):
#     print(f'Hello, {to}')

# # function are defined first then we can use further in code
# hello()
# name = input("What's your name? ")
# hello(name)


def main():
    name = input("What's your name? ")
    hello(name)

def hello(to='World'):
    print(f"Hello, {to}")

hello()
main()




