# LeetCode 23: Merge k Sorted Lists
# Approach: Min-Heap / Priority Queue | Time: O(N log k) | Space: O(k)

import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []

        # Push head of each non-empty list (use index i as tie-breaker for ListNode)
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        curr = dummy

        # Extract smallest node and push its next node
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


"""
Alternative Approach (Divide and Conquer):
Time: O(N log k) | Space: O(1)

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists:
            return None

        def mergeTwoLists(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
            dummy = ListNode(0)
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            curr.next = l1 or l2
            return dummy.next

        interval = 1
        while interval < len(lists):
            for i in range(0, len(lists) - interval, interval * 2):
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2

        return lists[0]
"""
