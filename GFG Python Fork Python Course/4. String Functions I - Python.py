def trim(str):
    return str.strip()


def exists(str, x):
    return str.find(x)


def titleIt(str):
    return str.title()


def casesSwap(str):
    return str.swapcase()


# {
# Driver Code Starts.


def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        str = input()
        x = input()
        str = trim(str)
        print(str)
        print(exists(str, x))
        print(titleIt(str))
        print(casesSwap(str))
        testcases -= 1


if __name__ == '__main__':
    main()