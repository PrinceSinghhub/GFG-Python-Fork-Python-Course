def isPrime(num):
    count = 2

    while count * count <= num:

        if num % count == 0:
            return False

        count += 1

    return True


# {
# Driver Code Starts.


import math  ##You will need this for prime checking


def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        number = int(input())
        print(isPrime(number))  ##This isPrime is function that you need to create
        testcases -= 1


if __name__ == '__main__':
    main()