def printIncreasingPower(x):
    ##Your code here

    # Loop to jump in powers of 2
    index = 1
    while True:
        if index ** 2 > x:
            break

        print(index ** 2, end=" ")
        index += 1

        ##Your code here


# {
# Driver Code Starts.
# Driver Code
def main():
    # Testcase input
    testcases = int(input())

    # Looping through testcases
    while (testcases > 0):
        x = int(input())

        printIncreasingPower(x);
        print()

        testcases -= 1


if __name__ == '__main__':
    main()