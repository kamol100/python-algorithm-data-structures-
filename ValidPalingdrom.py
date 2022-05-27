import re
def is_palindrome(s):
    start = ""

    s = re.sub(r'[^A-Za-z0-9]+',"",s).lower()
    i = len(s)-1

    while i >= 0:
        start += s[i].lower()

        i -= 1
    if s == start:
        return True
    else:
        return False


print(is_palindrome("A man, a plan, a  canal: Panama"))
print(is_palindrome("0p"))
