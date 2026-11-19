# LeetCode 31: Next Permutation
# Approach: Two Pointers (In-Place) | Time: O(n) | Space: O(1)

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first decreasing element from the right
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # Step 2: Find the smallest element larger than nums[i] to its right and swap
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Step 3: Reverse the suffix to get the smallest lexicographical order
        nums[i + 1:] = reversed(nums[i + 1:])
