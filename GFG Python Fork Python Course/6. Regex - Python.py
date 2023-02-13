# import re
#
# # todo find all int same manner il list form
# pat=re.compile('\d+')
# a = "asdasd123asmdasdk34234kfdsd34sdfk5"
# print(re.findall(pat,a))


import re


def numberMatcher(str):
    pat = re.compile('\d+')
    match = re.findall(pat, str)  ##find all finds all the matched texts and returns a list
    if (match):
        for i in match:
            print(i, end=" ")
    else:
        print(-1, end="")


# {
# Driver Code Starts.

def main():
    testcases = int(input())  # testcases
    while (testcases > 0):
        str = input()
        numberMatcher(str)
        print()
        testcases -= 1


if __name__ == '__main__':
    main()