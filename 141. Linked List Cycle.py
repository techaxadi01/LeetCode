# LeetCode 141: Linked List Cycle
# Approach: Fast & Slow Pointers (Floyd's Cycle Finding) | Time: O(n) | Space: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:
        slow = fast = head

        # Fast moves 2 steps, slow moves 1 step
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If pointers meet, a cycle exists
            if slow is fast:
                return True

        return False
