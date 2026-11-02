# LeetCode 462: Minimum Moves to Equal Array Elements II
# Approach: Sorting (Median) | Time: O(n log n) | Space: O(1)

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        med = nums[len(nums) // 2]  # Median minimizes total distance
        steps = 0

        # Sum moves needed to bring all numbers to the median
        for num in nums:
            steps += abs(med - num)

        return steps
