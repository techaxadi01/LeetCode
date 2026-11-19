# LeetCode 215: Kth Largest Element in an Array
# Approach: Min-Heap of Size k | Time: O(n log k) | Space: O(k)

import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []  # Maintain k largest elements seen so far

        for num in nums:
            heapq.heappush(min_heap, num)

            # Evict smallest element when heap exceeds size k
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Root of min-heap is the kth largest element
        return min_heap[0]


"""
Alternative Approach (Quickselect):
Time: O(n) average, O(n^2) worst-case | Space: O(1)

import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        target = len(nums) - k  # Convert kth largest to index in 0-indexed sorted order

        def quickselect(l: int, r: int) -> int:
            pivot_idx = random.randint(l, r)
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[r] = nums[r], nums[pivot_idx]

            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[r] = nums[r], nums[p]

            if p == target:
                return nums[p]
            elif p < target:
                return quickselect(p + 1, r)
            else:
                return quickselect(l, p - 1)

        return quickselect(0, len(nums) - 1)
"""
