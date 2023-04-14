# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow: #If it is cyclic, reset the slow pointer to head
                slow = head
                while slow != fast:#Move pointers at the same pace till they meet once more and return the index
                    slow = slow.next
                    fast = fast.next
                return slow
        return None   