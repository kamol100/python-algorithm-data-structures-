def str_str(haystack, needle):
    match = haystack[:len(needle)]
    for i in range(len(haystack)):
        if match == needle:
            if i > 1:
                return i -1
            return i
        else:
            match = haystack[i:len(needle)+i]
        if i == len(haystack)-1 and needle == haystack[len(haystack)-1]:
            return i
    return -1






print(str_str("hellio", "o"))
print(str_str("mississippi", "issip"))
