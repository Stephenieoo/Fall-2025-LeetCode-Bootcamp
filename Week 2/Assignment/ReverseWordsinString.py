'''
Input: s = "the sky is blue"
Output: "blue is sky the"

Input: s = "  hello world  "
Output: "world hello"

'''
def main(s):
    i = 0
    n = len(s)
    res = []
    while i < n:
        while i < n and s[i] == ' ':
            i += 1
        j = i
        while j < n and s[j] != ' ':
            j += 1
        if i!=j:
            res.append(s[i:j])
        i = j
    print(len(res))
    return ' '.join(res[::-1])

print(main("the sky is blue"))
print(main("  hello world  "))