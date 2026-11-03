# LeetCode 3736: Minimum Moves to Equal Array Elements III
# Approach: Math | Time: O(n) | Space: O(1)

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        sum_num = sum(nums)              # Sum of current elements
        max_sum = max(nums) * len(nums)  # Target sum when all elements equal the max
        steps = max_sum - sum_num        # Moves needed to reach target sum
        return steps

        # One-line Mathematical Solution:
        # return max(nums) * len(nums) - sum(nums)

"""
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        step = 0
        maxele = max(nums)
        for num in nums:
            step += maxele - num
        return step
"""