def welcomeAboard(name):
    print("Welcome", name)  # Your code here


# {
# Driver Code Starts.
# Driver Code
def main():
    # Testcase input
    testcases = int(input())

    # Looping through testcases
    while (testcases > 0):
        name = input()

        welcomeAboard(name);

        testcases -= 1


if __name__ == '__main__':
    main()