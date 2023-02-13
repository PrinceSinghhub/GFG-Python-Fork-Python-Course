def count_even_odd(N, arr):
    c_e = 0
    c_o = 0

    pair = list()

    # your code here

    for i in arr:
        if i % 2 == 0:
            c_e += 1
        else:
            c_o += 1

    pair.append(c_e)
    pair.append(c_o)

    return pair


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

        # calling function to count even odd
        a = count_even_odd(N, arr)
        print(a[0], a[1])
        testcases -= 1


if __name__ == '__main__':
    main()
# } Driver Code Ends