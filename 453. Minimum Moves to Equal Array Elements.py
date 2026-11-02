# LeetCode 453: Minimum Moves to Equal Array Elements
# Approach: Math | Time: O(n) | Space: O(1)

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_val = min(nums)  # Smallest element in the array
        step = 0

        # Incrementing n-1 elements is equivalent to decrementing each to min_val
        for num in nums:
            step += num - min_val

        return step


"""
One-line Mathematical Solution:
Time: O(n) | Space: O(1)

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        # Total moves = sum(nums) - n * min(nums)
        return sum(nums) - min(nums) * len(nums)
"""
