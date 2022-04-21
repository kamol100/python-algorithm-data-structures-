def length_of_longest_substring(s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        maps = []
        ll = 0
        for (i,ch) in enumerate(s):
            while ch in maps:
                maps.pop(0)
            maps.append(ch)
        
            if ll < len(maps):
                ll = len(maps)
            print(maps)


        return ll



print(length_of_longest_substring('abcabcdbb'))
print(length_of_longest_substring('pwwkew'))
print(length_of_longest_substring('au'))
print(length_of_longest_substring('aab'))
print(length_of_longest_substring('dvdf'))
print(length_of_longest_substring('qrsvbspk'))
