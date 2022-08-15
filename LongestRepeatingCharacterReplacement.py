def character_replacement_optimize(strs, k):
    count = {}
    res = 0
    l = 0
    maxFrequency = 0
    for r in range(len(strs)):
        count[strs[r]] = 1 + count.get(strs[r], 0)
        maxFrequency = max(maxFrequency, count[strs[r]])
        if (r - l + 1) - maxFrequency > k:
            count[strs[l]] = -1
            l += 1
        res = max(res, r-l + 1)
    return res



def character_replacement(strs, k):
    count = {}
    res = 0
    l = 0
    for r in range(len(strs)):
        count[strs[r]] = 1 + count.get(strs[r], 0)
        if (r - l + 1) - max(count.values()) > k:
            count[strs[l]] -= 1
            l += 1
        res = max(res, r-l+1)
    return res






print(character_replacement_optimize("AABABBA", 1))
print(character_replacement("AABABBA", 1))
