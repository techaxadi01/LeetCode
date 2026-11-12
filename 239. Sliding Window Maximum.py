# LeetCode 239: Sliding Window Maximum
# Approach: Max-Heap (Lazy Deletion) | Time: O(n log n) | Space: O(n)

import heapq


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        heap = []  # Max-heap storing (-value, index)
        res = []

        for i, num in enumerate(nums):
            heapq.heappush(heap, (-num, i))

            # Lazily remove elements outside the current window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            # Record window maximum once the first window of size k is formed
            if i >= k - 1:
                res.append(-heap[0][0])

        return res


"""
Optimal Approach (Monotonic Decreasing Deque):
Time: O(n) | Space: O(k)

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()  # Stores indices of potential maximums in decreasing order
        res = []

        for i, num in enumerate(nums):
            # Remove index that fell outside the current window
            if dq and dq[0] <= i - k:
                dq.popleft()

            # Maintain decreasing order: discard smaller elements from the back
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            dq.append(i)

            # Front of deque holds the maximum for the current window
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res
"""
