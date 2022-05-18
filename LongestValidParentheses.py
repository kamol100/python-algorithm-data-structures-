def longest_valid_parentheses(s):
    count = 0
    stack = [-1]
    if len(s) < 1:
        return 0
    for i,p in enumerate(s):
        if p == "(":
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                count = max(count, i-stack[-1])
    return count


print(longest_valid_parentheses("()"))
print("=============")
print(longest_valid_parentheses("()(())"))
print("=============")
print(longest_valid_parentheses("(()()"))
print("=============")
print(longest_valid_parentheses("()(((()((((()"))
print("==============")
print(longest_valid_parentheses("()((()))()()"))
