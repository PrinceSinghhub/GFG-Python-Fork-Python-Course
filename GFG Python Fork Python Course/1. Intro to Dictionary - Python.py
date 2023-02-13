def create_dict(arr):
    dict = {}

    for i in range(len(arr)):
        dict[arr[i][0]] = arr[i][1]

    return dict


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

        dict = create_dict(arr)

        for key in sorted(dict.keys()):
            print(key, dict[key])

        testcases -= 1


if __name__ == '__main__':
    main()