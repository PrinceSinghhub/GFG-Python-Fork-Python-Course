def number_present(num_list, Q):
    if Q in num_list:
        return True


# {
# Driver Code Starts.
def main():
    testcases = int(input())
    while testcases:
        num_list = input()
        num_list = num_list.split()
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])

        q = input()
        q = q.split()
        for i in range(len(q)):
            q[i] = int(q[i])

        for i in range(len(q)):
            if number_present(num_list, q[i]):
                print("True")
            else:
                print("False")
        testcases -= 1


if __name__ == '__main__':
    main()