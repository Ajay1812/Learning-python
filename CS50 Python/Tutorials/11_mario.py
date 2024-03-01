def main():
    # print_columns(3)

# def print_columns(height):
#     for _ in range(height):
#         print("#" * height, end="")
    print_rows(3)

def print_rows(rows):
    # for _ in range(rows):
    #     print("# " * rows, end="\n")

    for i in range(rows):
        for j in range(rows):
            print("? ", end="")
        print()

main()