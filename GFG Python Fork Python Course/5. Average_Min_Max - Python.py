def calc_average(arr):
    arr.remove(max(arr))
    arr.remove(min(arr))

    return sum(arr) // len(arr)


# {
#  Driver Code Starts
# Initial Template for Python 3


# Driver Code
if __name__ == '__main__':
    # Testcase input
    testcases = int(input())
    # Looping through testcases
    while (testcases > 0):
        N = int(input())

        a = list(map(int, input().strip().split()))

        print(calc_average(a))

        testcases -= 1