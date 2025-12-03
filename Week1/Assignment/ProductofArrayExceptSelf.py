from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n
    
    # the left product
    for i in range(1, n):
        res[i] = res[i - 1] * nums[i - 1]
    
    # the right product
    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]
    
    return res

ns1 = [1,2,3,4]
ns2 = [-1,1,0,-3,3]
print(productExceptSelf(ns1))
print(productExceptSelf(ns2))