# LeetCode 739: Daily Temperatures
# Approach: Monotonic Decreasing Stack | Time: O(n) | Space: O(n)

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        stack = []  # Stores indices of days

        for i in range(n):
            # Pop colder days and record the days waited
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                ans[prev] = i - prev
            stack.append(i)

        return ans


"""
O(n^2) Time Complexity Solution:

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        ans = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if temperatures[i] < temperatures[j]:
                    ans[i] = j - i
                    break
        return ans
"""
