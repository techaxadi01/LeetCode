// LeetCode 2: Add Two Numbers
// Approach: Elementary Math / Simulation | Time: O(max(m, n)) | Space: O(max(m, n))

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2) {
    struct ListNode* head = NULL;
    struct ListNode* curr = NULL;
    int carry = 0;

    // Traverse both lists and process any remaining carry
    while (l1 != NULL || l2 != NULL || carry != 0) {
        int sum = carry;

        // Add l1 value if available
        if (l1 != NULL) {
            sum += l1->val;
            l1 = l1->next;
        }

        // Add l2 value if available
        if (l2 != NULL) {
            sum += l2->val;
            l2 = l2->next;
        }

        struct ListNode* newNode = malloc(sizeof(struct ListNode));
        if (newNode == NULL) {
            return head;
        }

        newNode->val = sum % 10;
        newNode->next = NULL;
        carry = sum / 10;  // Carry for the next place value

        // Attach new node to the result list
        if (head == NULL) {
            head = newNode;
            curr = newNode;
        } else {
            curr->next = newNode;
            curr = newNode;
        }
    }

    return head;
}
