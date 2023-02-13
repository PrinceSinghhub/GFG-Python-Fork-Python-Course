def print_elements(N, arr):
    mid = N // 2

    for i in range(mid):
        print(arr[i], end=" ")

    for j in range(mid, N, 3):
        print(arr[j], end=" ")

    # Your code here
    # use '//' to divide to get int for index


# {
# Driver Code Starts.
# Driver Code
def main():
    # Testcase input
    testcases = int(input())

    # Looping through testcases
    while (testcases > 0):
        # size of array
        N = int(input())

        # array elements input
        array = input().split()
        # print (array)
        arr = list()
        for i in array:
            arr.append(int(i))

        # print (arr)

        # calling function to print elements
        print_elements(N, arr)
        print()
        testcases -= 1


if __name__ == '__main__':
    main()