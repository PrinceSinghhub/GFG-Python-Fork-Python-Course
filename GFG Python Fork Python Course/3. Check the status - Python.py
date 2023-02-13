def check_status(a, b, flag):
    if (a > 0 and b > 0):
        return False
    elif ((a > 0 or b > 0) and flag == False) or ((a < 0 and b < 0) and flag == True):
        return True
    else:
        return False

    ##Your code here
    ##Either True or False is returned


# {
# Driver Code Starts.

# Driver Code
def main():
    # Testcase input
    testcases = int(input())

    # Looping through testcases
    while (testcases > 0):
        a = int(input())
        b = int(input())
        flag = input()

        if (flag == "True"):
            flag = True
        else:
            flag = False

        if (check_status(a, b, flag) is True):
            print("True")
        else:
            print("False")

        testcases -= 1


if __name__ == '__main__':
    main()