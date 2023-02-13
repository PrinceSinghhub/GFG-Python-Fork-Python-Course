def customSort(arr):
    return sorted(arr)

    # Your code here
    # Hint : Should be a return statement


# {
# Driver Code Starts.

# Driver Code
def main():
    # Testcase input
    testcases = int(input())

    # Looping through testcases
    while (testcases > 0):
        N = int(input())

        name = input().split()
        marks = input().split()
        arr = list()
        for i in range(0, N, 1):
            arr.append((name[i], marks[i]))

        arr.sort(key=customSort)

        for i in arr:
            print(i[0], i[1], end=" ")

        print()
        testcases -= 1


if __name__ == '__main__':
    main()