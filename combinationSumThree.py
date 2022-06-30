#problem-216
#https://leetcode.com/problems/combination-sum-iii/
def combination_sum(k, n):
    res = []

    def backtrack(num, stack, target):
        if stack and len(stack) == k and target == 0:
            res.append(stack.copy())
            return
        if target <= 0:
            return
        for i in range(num + 1, 10):
            stack.append(i)
            backtrack(i, stack, target - i)
            stack.pop()

    backtrack(0, [], n)
    return res


print(combination_sum(3,7))
print(combination_sum(9,45))
