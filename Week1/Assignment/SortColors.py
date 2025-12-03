from typing import List


def sortColors(nums: List[int]) -> None:
    n = len(nums)
    # l: next position to place 0
    # mid: number currently being processed
    # r: next position to place 2
    l, mid, r = 0, 0, n-1
    while mid <= r:
        if nums[mid] == 0:
            nums[mid], nums[l] = nums[l], nums[mid]
            l += 1
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[r] = nums[r], nums[mid]
            r -= 1
        else:
            mid += 1
    return nums

ns1 = [2,0,2,1,1,0]
print(sortColors(ns1))

ns2 = [1,2,0]
print(sortColors(ns2))