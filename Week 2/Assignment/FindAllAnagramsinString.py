'''
Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with s
'''
from typing import Counter

# brute-force
def bruteForce(s, p):
    count_p = Counter(p)
    m = len(s)
    n = len(p)
    res = []
    for i in range(m-n+1):
        count_s = Counter(s[i:i+n])
        if count_s == count_p:
            res.append(i)
    return res

def twoPointers(s, p):
    count_p = Counter(p)
    m = len(s)
    n = len(p)
    res = []
    count_s = Counter(s[:n])
    if count_s == count_p:
        res.append(0)
    for i in range(n, m):
        
        count_s[s[i]] += 1
        # print("s:", count_s)
        # the char at the left boundary
        ch = s[i-n]
        count_s[ch] -= 1
        
        if count_s[ch] == 0:
            del count_s[ch]
        print("i:",i,",s:", count_s)
        if count_s == count_p:
            res.append(i-n+1)
    return res

# def main2()
# print(bruteForce("cbaebabacd", "abc"))
print(twoPointers("cbaebabacd", "abc"))