def printInDecreasing(x):
    # Complete the code below
    while (x >= 0):
        print(x, end=" ")

        # your statement below to print the number
        # in decreasing order
        # Note: use end=" " parameter with print to seperate numbers by space.
        ##Output for testcases will automatically separated by a new line by the print() in driver code

        x -= 1


# {
# Driver Code Starts.
# Driver Code
def main():
    # Testcase input
    testcases = int(input())

    # Looping through testcases
    while (testcases > 0):
        x = int(input())

        printInDecreasing(x);

        print()

        testcases -= 1


if __name__ == '__main__':
    main()
# } Driver Co