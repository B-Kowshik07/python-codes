import re

def isPalindrome(string):
    string = re.sub(r'[^A-Za-z0-9]', '', string).lower()
    l, r = 0, len(string) - 1

    while l <= r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True
string=input()
print(isPalindrome(string))