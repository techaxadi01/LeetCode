# LeetCode 94: Binary Tree Inorder Traversal
# Approach: Recursive Depth-First Search (DFS) | Time: O(n) | Space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        ino = []

        # Inorder: Left subtree -> Root -> Right subtree
        if root is not None:
            ino.extend(self.inorderTraversal(root.left))
            ino.append(root.val)
            ino.extend(self.inorderTraversal(root.right))

        return ino


"""
Alternative Approach (Iterative using Stack):
Time: O(n) | Space: O(n)

class Solution:
    def inorderTraversal(self, root: TreeNode | None) -> list[int]:
        res = []
        stack = []
        curr = root

        while curr or stack:
            # Reach the leftmost node of the current subtree
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res
"""
