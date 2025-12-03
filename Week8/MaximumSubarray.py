class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_sum = cur= nums[0]
        for i in range(1, n):
            cur = max(nums[i], cur + nums[i])
            max_sum = max(max_sum, cur)
        return max_sum