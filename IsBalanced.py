def isBalanced(s):
    stack = []

    if len(s)%2 != 0:
        return "NO"
    brac = {
        '{':'}',
        '[':']',
        '(':')'
    }
    
    for  char in s:
        if char in ['{','[','(']:
            stack.append(char)
        else:
            if stack:
               top = stack.pop()
               if brac[top] != char:
                   return "NO"
    return "NO" if stack else "YES"



s = '{([)]}'
print(isBalanced(s))
print("=====================")
s = '{(([])[])[]}'
print(isBalanced(s))