# LeetCode 22: Generate Parentheses
# Approach: Backtracking / DFS | Time: O(4^n / sqrt(n)) | Space: O(n)

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(s: str, open_count: int, close_count: int) -> None:
            # Base case: valid combination of length 2n reached
            if len(s) == 2 * n:
                res.append(s)
                return

            # Can add '(' if we haven't placed all n open brackets
            if open_count < n:
                backtrack(s + "(", open_count + 1, close_count)

            # Can add ')' only if it doesn't exceed placed '('
            if close_count < open_count:
                backtrack(s + ")", open_count, close_count + 1)

        backtrack("", 0, 0)
        return res


"""
Alternative Approach (Dynamic Programming):
Time: O(4^n / sqrt(n)) | Space: O(4^n / sqrt(n))

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for i in range(1, n + 1):
            for c in range(i):
                for left in dp[c]:
                    for right in dp[i - 1 - c]:
                        dp[i].append(f"({left}){right}")

        return dp[n]
"""
