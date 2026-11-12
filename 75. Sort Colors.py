# LeetCode 75: Sort Colors
# Approach: In-Place Pop & Insert/Append | Time: O(n^2) | Space: O(1)

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = -1
        for _ in range(len(nums)):
            i += 1
            if nums[i] == 0:
                nums.insert(0, nums.pop(i))  # Move 0s to the front
            elif nums[i] == 2:
                nums.append(nums.pop(i))     # Move 2s to the back
                i -= 1                       # Re-check element shifted into index i


"""
Optimal Approach (Dutch National Flag / Three Pointers):
Time: O(n) | Space: O(1)

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1  # Re-check swapped element from high
"""
