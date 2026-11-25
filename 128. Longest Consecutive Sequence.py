# LeetCode 128: Longest Consecutive Sequence
# Approach: Hash Set (Start-of-Sequence Check) | Time: O(n) | Space: O(n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s = set(nums)
        longest = 0

        for num in s:
            # Only start counting if num is the beginning of a sequence
            if num - 1 not in s:
                count = 1
                while num + count in s:
                    count += 1
                longest = max(longest, count)

        return longest


"""
Alternative Approach (Union-Find / Disjoint Set Union):
Time: O(n * α(n)) | Space: O(n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        parent = {}
        size = {}

        def find(i: int) -> int:
            if parent[i] != i:
                parent[i] = find(parent[i])
            return parent[i]

        def union(i: int, j: int) -> None:
            root_i, root_j = find(i), find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                size[root_j] += size[root_i]

        num_set = set(nums)
        for num in num_set:
            parent[num] = num
            size[num] = 1

        for num in num_set:
            if num + 1 in num_set:
                union(num, num + 1)

        return max(size.values())
"""
