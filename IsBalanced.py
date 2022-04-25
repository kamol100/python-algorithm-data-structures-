def isBalanced(s):
    stack = []

    if len(s)%2 != 0:
        return "NO"
    brac = {
        '{':'}',
        '[':']',
        '(':')'
    }
    item = 0
    for  char in s:
        if char in ['{','[','(']:
            stack.append(char)
            item += 1
        else:
            if stack:
               top = stack.pop()
               item += 1
               if brac[top] != char:
                   return "NO"
    if item == 0 or item < len(s):
        return "NO"
    print(stack,item, len(s))
    return "NO" if stack else "YES"



s = '(((])))'
print(isBalanced(s))
print("=====================")
s = '{(([])[])[]}'
print(isBalanced(s))