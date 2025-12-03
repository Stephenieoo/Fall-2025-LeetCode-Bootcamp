def myAtoi(self, s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    sign = 1
    i = 0
    while i < n and s[i] == ' ':
        i += 1
    if i < n and s[i] in ['-', '+']:
        if s[i] == '-':
            sign = -1
        i += 1
    
    num = 0
    for j in range(i, n):
        if s[j].isdigit():
            print(s[j])
            num = num * 10 + int(s[j])
        else:
            break
    max_int, min_int = 2**31 - 1, -2**31
    
    if sign * num > 2**31 - 1:
        return 2**31 - 1
    if sign * num < -2**31:
        return -2**31
    return sign * num
    


