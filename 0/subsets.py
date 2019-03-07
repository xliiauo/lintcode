def subsets(s1, s2):
    results = []
    lst = []
    helper(results, lst, s1, 0)

    cur_max = ''
    for string in results:
        if string in s2 and len(string) > len(cur_max):
            cur_max = string

    return cur_max


def helper(results, lst, string, pos):
    results.append(''.join(list(lst)))

    for i in range(pos, len(string)):
        lst.append(string[i])
        helper(results, lst, string, i + 1)
        lst.pop()

print(subsets('abc', 'abdc'))
print(subsets('abc', 'dabc'))
