def multivar(n, *var):
    print(n + sum(var))


# {
# Driver Code Starts.


def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        single = int(input())
        multivar(single, 4, 5, 6, 7)  ## The single argument and multiarguments are passed to multivar function
        testcases -= 1


if __name__ == '__main__':
    main()