# LeetCode 100: Same Tree
# Approach: Recursive Depth-First Search (DFS) | Time: O(min(m, n)) | Space: O(min(h1, h2))

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        # Both trees are empty -> identical
        if not p and not q:
            return True

        # One tree is empty or root values differ -> not identical
        if not p or not q or p.val != q.val:
            return False

        # Recursively verify both left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


"""
Alternative Approach (Iterative BFS using Deque):
Time: O(min(m, n)) | Space: O(min(m, n))

from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        queue = deque([(p, q)])

        while queue:
            node_p, node_q = queue.popleft()

            if not node_p and not node_q:
                continue
            if not node_p or not node_q or node_p.val != node_q.val:
                return False

            queue.append((node_p.left, node_q.left))
            queue.append((node_p.right, node_q.right))

        return True
"""
