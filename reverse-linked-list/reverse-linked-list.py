# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head #Previous node is null, current node is the head node
        
        while curr: #while current node is not null
            nxt = curr.next #Put in a holding variable
            curr.next = prev #Change the next pointer to previous
            prev = curr #Move previous node to current node
            curr = nxt #Move current node to next node
        return prev    