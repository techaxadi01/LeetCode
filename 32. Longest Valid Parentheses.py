# LeetCode 32: Longest Valid Parentheses
# Approach: Stack | Time: O(n) | Space: O(n)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # Base index for valid substring length calculation
        ans = 0

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                # If stack is empty, current ')' is a new boundary index
                if not stack:
                    stack.append(i)
                else:
                    ans = max(ans, i - stack[-1])

        return ans


"""
Optimal Approach (Two-Pass Left & Right Counters):
Time: O(n) | Space: O(1)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = max_len = 0

        # Left-to-right pass
        for ch in s:
            if ch == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * right)
            elif right > left:
                left = right = 0

        # Right-to-left pass
        left = right = 0
        for ch in reversed(s):
            if ch == '(':
                left += 1
            else:
                right += 1

            if left == right:
                max_len = max(max_len, 2 * left)
            elif left > right:
                left = right = 0

        return max_len
"""
