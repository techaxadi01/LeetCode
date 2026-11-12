# LeetCode 3105: Longest Strictly Increasing or Strictly Decreasing Subarray
# Approach: One Pass | Time: O(n) | Space: O(1)

class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        inc = dec = ans = 1  # Track current increasing, decreasing, and max lengths

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc += 1  # Extend increasing streak, reset decreasing
                dec = 1
            elif nums[i] < nums[i - 1]:
                dec += 1  # Extend decreasing streak, reset increasing
                inc = 1
            else:
                inc = dec = 1  # Equal elements break both strict streaks

            ans = max(ans, inc, dec)

        return ans
