def join_middle(bound_by, tag_name):
    mid = len(bound_by) // 2
    # complete the statement below to return the string as required
    return bound_by[0:  mid] + tag_name + bound_by[mid: len(bound_by) + 1]


# {
# Driver Code Starts.
# Driver Code
def main():
    # testcase input
    testcases = int(input())

    # looping through testcases
    while (testcases > 0):
        string = input().split()
        bound_by = string[0]
        tag_name = string[1]

        testcases -= 1

        print(join_middle(bound_by, tag_name))


if __name__ == '__main__':
    main()