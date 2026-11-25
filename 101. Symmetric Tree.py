# LeetCode 101: Symmetric Tree
# Approach: Recursive DFS (Mirror Check) | Time: O(n) | Space: O(h)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        def is_mirror(t1: TreeNode | None, t2: TreeNode | None) -> bool:
            # Both subtrees empty -> symmetric
            if not t1 and not t2:
                return True

            # One empty or root values mismatch -> asymmetric
            if not t1 or not t2 or t1.val != t2.val:
                return False

            # Outer children (t1.left, t2.right) and inner children (t1.right, t2.left) must mirror
            return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

        return is_mirror(root.left, root.right) if root else True


"""
Alternative Approach (Iterative BFS using Deque):
Time: O(n) | Space: O(n)

from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        if not root:
            return True

        queue = deque([(root.left, root.right)])

        while queue:
            t1, t2 = queue.popleft()

            if not t1 and not t2:
                continue
            if not t1 or not t2 or t1.val != t2.val:
                return False

            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))

        return True
"""
