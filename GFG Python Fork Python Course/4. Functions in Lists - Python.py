def sort_arr(arr):
    arr.sort()
    # Your code here


# Function to join list elements
# with string as delimiter
def join_list(arr, string):
    return string.join(arr)


# Function to reverse array elements
def rev_arr(arr):
    return arr.reverse()

    # Your code here


# Function to insert element at index
def insert_arr(arr, index, element):
    # Your code here
    arr.insert(index, element)
    return arr


# Function to pop element from array at index
def pop_arr(arr, index):
    arr.pop(index)
    return arr


# {
# Driver Code Starts.
# Driver Code
def main():
    # Testcase input
    testcases = int(input())

    # Looping through testcases
    while (testcases > 0):
        # size of array and query
        N_and_Q = input().split()
        N = int(N_and_Q[0])
        Q = int(N_and_Q[1])

        # array elements input
        array = input().split()

        arr = list()
        for i in array:
            arr.append(i)

        # looping through each query
        for i in range(0, Q, 1):
            query = input().split()
            op = query[0]

            if (op == 'i'):
                index = int(query[1])
                element = query[2]
                insert_arr(arr, index, element)

            if (op == 'p'):
                index = int(query[1])
                pop_arr(arr, index)

            if (op == 'j'):
                string = query[1]
                print(join_list(arr, string))

            if (op == 'r'):
                rev_arr(arr)

            if (op == 's'):
                sort_arr(arr)

        for i in arr:
            print(i, end=' ')

        print()

        testcases -= 1


if __name__ == '__main__':
    main()