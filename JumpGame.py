def can_jump(nums):
    goal = len(nums) -1
    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= goal:
            goal = i
        print(i + nums[i], goal, i)
    return True if goal == 0 else False

print(can_jump([2,3,1,1,4])) #true
print(can_jump([2,3,0,1,4])) #true
print(can_jump([3,2,1,0,4])) #false
print(can_jump([2,0])) #true
print(can_jump([2,0,0])) #true
print(can_jump([1,1,0])) #true



