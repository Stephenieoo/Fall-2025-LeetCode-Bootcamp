from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    n = len(numbers)
    l, r = 0, n-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l + 1, r + 1]
        elif s > target:
            r -= 1
        else:
            l += 1

ns1 = [2,7,11,15]
t1 = 9
ns2 = [2,3,4]
t2 = 6
print(twoSum(ns1, t1))
print(twoSum(ns2, t2))