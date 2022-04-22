def longest_common_prefix(strs):
    result = strs[0]
    for i in range(len(strs)-1):
        str1 = strs[i]
        str2 = strs[i+1]
        temp = ""
        for (j,k) in zip(str1, str2):
            if j == k:
                temp +=j
            else:
                break
        if len(result) > len(temp):
            result = temp

    return result



strs  = ["flower","flow","flight"]
print(longest_common_prefix(strs))
strs  = ["dog","racecar","car"]
print(longest_common_prefix(strs))
strs  = ["cir","car"]
print(longest_common_prefix(strs))
strs  = ["a","a","b"]
print(longest_common_prefix(strs))
