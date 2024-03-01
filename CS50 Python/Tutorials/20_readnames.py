# with open("names.txt", 'r') as file:
#     lines = file.readlines()

# for line in lines:
#     # print("Hello ",line, end='')
#     print("Hello,",line.rstrip())

with open("names.txt", 'r') as file:
    for line in sorted(file, reverse=True):
        print("Hello,", line.rstrip())