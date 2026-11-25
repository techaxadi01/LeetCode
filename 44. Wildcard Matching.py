# LeetCode 44: Wildcard Matching
# Approach: Greedy Two Pointers | Time: O(m * n) worst-case, O(m + n) average | Space: O(1)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        star = -1
        match = 0

        while i < len(s):
            # Case 1: Exact character match or '?' wildcard
            if j < len(p) and (p[j] == s[i] or p[j] == '?'):
                i += 1
                j += 1
            # Case 2: Encountered '*' wildcard -> greedily match 0 characters first
            elif j < len(p) and p[j] == '*':
                star = j
                match = i
                j += 1
            # Case 3: Mismatch after '*' -> backtrack and let '*' consume one more character
            elif star != -1:
                j = star + 1
                match += 1
                i = match
            # Case 4: Mismatch with no previous '*' to backtrack to
            else:
                return False

        # Consume any remaining '*' characters in pattern
        while j < len(p) and p[j] == '*':
            j += 1

        return j == len(p)


"""
Alternative Approach (Dynamic Programming - 1D Array):
Time: O(m * n) | Space: O(n)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [False] * (n + 1)
        dp[0] = True

        # Handle leading '*' in pattern
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                dp[j] = dp[j - 1]

        for i in range(1, m + 1):
            prev = dp[0]
            dp[0] = False
            for j in range(1, n + 1):
                temp = dp[j]
                if p[j - 1] == '*':
                    dp[j] = dp[j] or dp[j - 1]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[j] = prev
                else:
                    dp[j] = False
                prev = temp

        return dp[n]
"""
