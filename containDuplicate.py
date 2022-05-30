def contains_duplicate(nums):
    dic = {}
    for index,i in enumerate(nums):
        if i in dic:
            return True
        else:
            dic[i] = index
        #print(dic)
    return False

def contains_duplicate2(nums):
    return len(nums) != len(set(nums))

print(contains_duplicate2([1,2,3]))
print(contains_duplicate2([1,1,2,3]))
