def matching_string(strings, queries):
    maps = {}
    for q in queries:
        for s in strings:
            if q not in maps:
                maps[q]:1
            else:
                maps[q] += 1
    print(maps)


print(matching_string(['ab', 'ab', 'abc'], ['ab', 'abc', 'bc']))