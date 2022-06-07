def repeated_substring_pattern(s):
    ds = (s+s)[1:-1]
    print(ds)
    return s in ds






print(repeated_substring_pattern("abab"))
print(repeated_substring_pattern("abcabcabcabc"))
