class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        
        # dp[i] = number of people who **learn** the secret on day i
        dp = [0] * (n + 1)
        dp[1] = 1  # On day 1, exactly one person knows the secret
        
        # share = number of people who currently know the secret
        #         AND are still in the "sharing window" on a given day
        #
        # People who learned on day j will:
        #   - start sharing on day (j + delay)
        #   - stop sharing (forget) on day (j + forget)
        share = 0
        
        # Iterate over each day to compute how many new people learn the secret
        for day in range(2, n + 1):
            # People who learned on (day - delay) start sharing today
            if day - delay >= 1:
                share = (share + dp[day - delay]) % MOD
            
            # People who learned on (day - forget) forget the secret today,
            # so they stop sharing
            if day - forget >= 1:
                share = (share - dp[day - forget]) % MOD
            
            # All people who are currently sharing will teach the secret
            # to the same number of new people today
            dp[day] = share
        
        # At the end (day n), some people have already forgotten the secret.
        # We only count those who **still remember** it.
        #
        # A person who learned on day i will forget on day (i + forget),
        # so on day n they still remember if:
        #   i + forget > n  =>  i > n - forget
        #
        # Therefore, we sum dp[i] for i in (n - forget + 1) ... n.
        start_day = max(1, n - forget + 1)
        result = sum(dp[start_day : n + 1]) % MOD
        
        return result