def is_anagram(s,t):
    dis = {}
    if len(s) != len(t):
        return False
    for i in s:
        #print(i,j)
        if i in dis:
            dis[i] += 1
        else:
            dis[i] = 1
    print(dis)
    for j in t:
        if j not in dis or dis[j] == 0:
            return False
        else:
            dis[j]-= 1
    return True



print(is_anagram("anagram", "nagaram"))
print(is_anagram("rat", "car"))
print(is_anagram("aacc", "ccac"))
