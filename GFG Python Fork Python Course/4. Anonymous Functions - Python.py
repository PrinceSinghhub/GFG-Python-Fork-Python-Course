power = lambda x, y: x ** y


# {
# Driver Code Starts.
def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        a = int(input())
        b = int(input())
        print(power(a, b))  ##calling the anonymous function
        testcases -= 1


if __name__ == '__main__':
    main()