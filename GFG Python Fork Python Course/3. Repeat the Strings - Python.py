def combo_string(a, b):
    if len(a) > len(b):
        return b + a + b
    else:
        return a + b + a


# {
# Driver Code Starts.
# Driver Code
def main():
    #
    testcases = int(input())

    while (testcases > 0):
        string = input().split()
        string1 = string[0]
        string2 = string[1]

        testcases -= 1

        print(combo_string(string1, string2))


if __name__ == '__main__':
    main()