def pair_sum(dict, N, arr, sum):
    # Your code here
    # Hint: You can use 'in' to find if any key is in dict
    for i in range(N):
        for j in range(i + 1, N):
            if arr[i] + arr[j] == sum:
                return True

    return False


# {
# Driver Code Starts.
# Driver code
def main():
    # testcase input
    testcase = int(input())

    # looping through testcases
    while (testcase > 0):

        N = int(input())
        sum = int(input())
        dict = {}
        x = N
        arr = [int(i) for i in (input().split())]

        for i in arr:
            dict[i] = 0

        for i in arr:
            dict[i] += 1

        if pair_sum(dict, N, arr, sum) is True:
            print("Yes")
        else:
            print("No")

        testcase -= 1


if __name__ == '__main__':
    main()