def pos(n):
    if n == 0:
        print("already Zero")

    else:
        for i in range(n - 1, -1, -1):
            print(i, end=" ")


def neg(n):
    if n == 0:
        print("already Zero")

    else:
        while n <= 0:
            print(n, end=" ")
            n += 1


# {
# Driver Code Starts.


def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        n = int(input())
        if (n > 0):
            pos(n)
        elif (n < 0):
            neg(n)
        else:
            print("already Zero", end="")
        print()
        testcases -= 1


if __name__ == '__main__':
    main()