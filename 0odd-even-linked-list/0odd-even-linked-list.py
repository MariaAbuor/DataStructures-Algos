# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = head #Set odd pointer to head
        if head is None: #If there is no head, return null head
            return head    
        even = head.next #Even node is one step after the head node
        evenhead = head.next #Store in a variable
        while even and even.next:
            odd.next = odd.next.next #Odd pointer skips a node
            odd = odd.next 
            even.next = even.next.next 
            even = even.next 
        odd.next = evenhead 
        return head