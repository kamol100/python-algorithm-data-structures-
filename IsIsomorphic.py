def is_isomorphic(s, t):
    mapST, mapTS = {},{}
    for c1, c2 in zip(s, t):
        if (c1 in mapST and mapTS[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1):
            return False
        mapTS[c1] = c2
        mapTS[c2] = c1
        print(mapTS)
        print(mapST)
    return True


print(is_isomorphic('arr', 'bcr'))
