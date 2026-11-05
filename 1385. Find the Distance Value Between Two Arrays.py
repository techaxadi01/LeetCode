# LeetCode 1385: Find the Distance Value Between Two Arrays
# Approach: Brute Force | Time: O(m * n) | Space: O(1)

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = len(arr1)  # Assume all elements satisfy the condition initially

        # Check each element in arr1 against all elements in arr2
        for a1 in arr1:
            for a2 in arr2:
                # If an element in arr2 is within distance d, exclude a1
                if abs(a1 - a2) <= d:
                    count -= 1
                    break

        return count
