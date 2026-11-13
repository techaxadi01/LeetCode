# LeetCode 164: Maximum Gap
# Approach: Sorting | Time: O(n log n) | Space: O(1)

class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        nums.sort()
        diff = 0

        # Check difference between every adjacent pair in sorted order
        for i in range(len(nums) - 1):
            diff = max(diff, nums[i + 1] - nums[i])

        return diff
