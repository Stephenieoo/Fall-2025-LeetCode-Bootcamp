class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # [1, 6, 17, 22]
        # []
        tot = sum(nums)
        if tot % 2 != 0: 
            return False
        target = tot // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for n in nums:
            for i in range(target, n - 1, -1):
                dp[i] = dp[i] or dp[i - n]
        return dp[-1]