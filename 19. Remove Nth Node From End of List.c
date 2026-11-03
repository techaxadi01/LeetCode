// LeetCode 19: Remove Nth Node From End of List
// Approach: Two Pointers (Fast & Slow) | Time: O(L) | Space: O(1)

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    // Dummy node handles edge cases like removing the head node
    struct ListNode dummy;
    dummy.next = head;

    struct ListNode* fast = &dummy;
    struct ListNode* slow = &dummy;

    // Advance fast pointer n steps ahead
    for (int i = 0; i < n; i++) {
        fast = fast->next;
    }

    // Move both pointers until fast reaches the last node
    while (fast->next != NULL) {
        fast = fast->next;
        slow = slow->next;
    }

    // Remove the target node and free its memory
    struct ListNode* temp = slow->next;
    slow->next = slow->next->next;
    free(temp);

    return dummy.next;
}
