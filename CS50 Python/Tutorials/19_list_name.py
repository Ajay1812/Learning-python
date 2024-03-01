
# names = []

# for _ in range(4):
#     name = input("What's your Name? ")
#     names.append(name)
# print(names)

# for name in sorted(names):
#     print(f"Hello, {name}")

names = []

for _ in range(4):
    name = input("What's your name? ")
    # names.append(name)
    with open("names.txt", "a") as file:
        file.write(f"{name}\n")