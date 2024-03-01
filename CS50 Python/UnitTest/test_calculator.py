from calculator import square

def main():
    test_square()

def test_square():
    # if square(2) != 4:
    #     print("2 squared was not 4")
    # if square(4) != 16:
    #     print("4 squared was not 16")
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 Squared is 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 Squared is 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 Squared is 0")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 Squared is 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 Squared is 4")
    
if __name__ == "__main__":
    main()