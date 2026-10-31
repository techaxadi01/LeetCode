# LeetCode 2016: Maximum Difference Between Increasing Elements
# Approach: One Pass / Greedy | Time: O(n) | Space: O(1)

class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        min_ele = nums[0]  # Smallest element seen so far
        max_diff = -1      # Default to -1 if no valid pair exists

        for num in nums:
            # If current element is larger, update maximum difference
            if min_ele < num:
                max_diff = max(max_diff, num - min_ele)
            else:
                min_ele = num  # Found a new smaller element

        return max_diff
