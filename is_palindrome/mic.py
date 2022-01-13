"""
1) compare the first char to the latest -> move to the center
2) find the mid position
3) need to check if odd or not
example - 12321
s = 12321
s2 = 12

s = 12
s2 = 12

"""

def isPalindrome(s):
    s2 = []
    mid = len(s) // 2
    for i in range(mid):
        s2.append(s.pop())
    if mid != 0:
        s.pop()
    for j in s:
        if s2.pop() != s.pop():
            return False
    else:
        return True


if __name__ == '__main__':
    test = [1,2,3,2,1]
    if isPalindrome(test):
        print("Yes")
    else:
        print("No")