def print_fun(string, x):
    print(string * x)


# {
# Driver Code Starts.

# Driver Code
def main():
    testcases = int(input())

    # Loop for testcases
    while (testcases > 0):
        string = input()
        x = int(input())
        print_fun(string, x)
        testcases -= 1


if __name__ == '__main__':
    main()