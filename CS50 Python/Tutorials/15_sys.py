import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few arrguments")
# elif len(sys.argv) > 2:
#     sys.exit("Too many arrguments")

# print("Hello, my name is", sys.argv[1])


if len(sys.argv) < 2 :
    print("Too few arrguments")

for arg in sys.argv[1:]:
    print("My name is ", arg)