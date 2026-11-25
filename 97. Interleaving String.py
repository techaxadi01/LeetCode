# LeetCode 97: Interleaving String
# Approach: Dynamic Programming (1D Space-Optimized) | Time: O(m * n) | Space: O(n)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        # Length check
        if m + n != len(s3):
            return False

        # dp[j] indicates if s1[:i] and s2[:j] can form s3[:i+j]
        dp = [False] * (n + 1)
        dp[0] = True

        # Base case: match using only s2
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            # Base case: match using only s1
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, n + 1):
                # Transition: choose character from s1 (dp[j]) or from s2 (dp[j-1])
                dp[j] = (
                    (dp[j] and s1[i - 1] == s3[i + j - 1]) or
                    (dp[j - 1] and s2[j - 1] == s3[i + j - 1])
                )

        return dp[n]


"""
Alternative Approach (Top-Down DP with Memoization):
Time: O(m * n) | Space: O(m * n)

from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        @cache
        def dfs(i: int, j: int) -> bool:
            if i == len(s1) and j == len(s2):
                return True

            choose_s1 = i < len(s1) and s1[i] == s3[i + j] and dfs(i + 1, j)
            choose_s2 = j < len(s2) and s2[j] == s3[i + j] and dfs(i, j + 1)

            return choose_s1 or choose_s2

        return dfs(0, 0)
"""
