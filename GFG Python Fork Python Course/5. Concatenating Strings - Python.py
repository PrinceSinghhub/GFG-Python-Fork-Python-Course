def print_fun(string1, string2):
    print(string1 + string2)


# {
# Driver Code Starts.

# Python Code to concatenate given strings
def main():
    testcases = int(input())

    while (testcases > 0):
        string1 = input()
        string2 = input()
        print_fun(string1, string2)

        testcases -= 1


if __name__ == '__main__':
    main()