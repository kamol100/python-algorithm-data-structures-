#given a string S, returns the index (counting from 0) of a character such that
# the part of the string to the left of that character is a reversal of the part of the string to its right.
#  The function should return −1 if no such index exists.
#Note: reversing an empty string (i.e. a string whose length is zero) gives an empty string.

def reverse_sub_string(strs):
    if len(strs) == 0 :return ''
    l,r = 0, len(strs)-1
    left_string = ''
    right_string = ''
    while l < r:
        left_string += strs[l]
        right_string += strs[r]
        l += 1
        r -= 1
    print(left_string, right_string)
    if left_string == right_string:
        return l
    else:
        return -1



print(reverse_sub_string("racecar"))