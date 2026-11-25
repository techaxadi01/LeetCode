# LeetCode 2567: Minimum Score by Changing Two Elements
# Approach: Sorting (Greedy) | Time: O(n log n) | Space: O(1)

class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        # Min score is achieved by modifying 2 elements (min diff can always be 0):
        # 1. Modify 2 smallest: max diff becomes nums[n-1] - nums[2]
        # 2. Modify 1 smallest & 1 largest: max diff becomes nums[n-2] - nums[1]
        # 3. Modify 2 largest: max diff becomes nums[n-3] - nums[0]
        return min(nums[n - 1] - nums[2], nums[n - 2] - nums[1], nums[n - 3] - nums[0])


"""
Optimal Approach (Finding 3 Smallest & 3 Largest Elements):
Time: O(n) | Space: O(1)

import heapq

class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        # Only need the 3 smallest and 3 largest elements
        smallest = sorted(heapq.nsmallest(3, nums))
        largest = sorted(heapq.nlargest(3, nums))

        return min(
            largest[2] - smallest[2],  # Modify 2 smallest elements
            largest[1] - smallest[1],  # Modify 1 smallest and 1 largest
            largest[0] - smallest[0]   # Modify 2 largest elements
        )
"""
