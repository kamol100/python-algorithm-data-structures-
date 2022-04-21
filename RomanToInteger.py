def roman_to_integer(s):
    maps = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    result = []
    for i in range(len(s)):
        if i > 0 and s[i-1]+s[i] in {"IV","IX","XL","XC","CD","CM"}:
            sub = maps[s[i]] - (maps[s[i-1]]*2)
            result.append(sub)
        else:
            result.append(maps[s[i]])
    print(result)
    return sum(result)




print(roman_to_integer("CMCD"))