# print("Meow")
# print("Meow")
# print("Meow")

# for _ in range(0,5):
#     print('Meow')

# i = 3
# while i!= 0:
#     print("Meow")
#     i = i - 1

# i = 1
# while i <= 3:
#     print("Meow")
#     i += 1 

# for i in [0,1,2,4]:
#     print('Meow')

# for _ in range(0,4):
#     print("Meow")

# print("Meow\n" *3, end='')

# while True: 
    
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print('Meow')

def main():
    number = get_number()
    meow(number)

def get_number():
    n = int(input("What's n? "))
    return n


def meow(n):
    for _ in range(n):
        print("Meow")

main()