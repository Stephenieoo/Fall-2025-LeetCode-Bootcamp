class Solution:
    def dailyTemperatures(self, temperatures):
        # Result array: res[i] = how many days to wait for a warmer temperature
        res = [0] * len(temperatures)

        # Monotonic stack: stores indices of days
        # Stack maintains decreasing temperatures (from bottom to top)
        stack = []

        # Iterate each day
        for i, t in enumerate(temperatures):

            # While current temperature is higher than the temperature at the index
            # on the top of the stack, it means we found a warmer day for that index.
            while stack and t > temperatures[stack[-1]]:
                prev = stack.pop()  # The previous day waiting for a warmer temp

                # Number of days between current day and that previous day
                res[prev] = i - prev

            # Push current day's index onto the stack
            stack.append(i)

        return res