def longest_paling_drome(s):
    result = ""
    longest = 0
    for i in range(len(s)):
        l, r = i,i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            print(l,r,s[l],s[r], r-l+1,i)
            if(r - l + 1) > longest:
                result = s[l:r+1]
                longest = r - l + 1

            l -= 1
            r += 1
        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if(r - l + 1) > longest:
                result = s[l:r+1]
                longest = r - l + 1
            l -= 1
            r += 1
        print("================",result)

    return result




strs = "babadlevelredivider"
# redivider, deified, civic, radar, level, rotor, kayak, reviver, racecar, madam, and refer.
print(longest_paling_drome(strs))