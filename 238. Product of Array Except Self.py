# LeetCode 238: Product of Array Except Self
# Approach: Prefix & Suffix Products | Time: O(n) | Space: O(1) [ignoring output]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)

        # Left pass: store product of all elements to the left of index i
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        # Right pass: multiply by product of all elements to the right of index i
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
