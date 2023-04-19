# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next = head) #Set a dummy node before the head of the list
        prev, curr = dummy, head #Initialize prev node as dummy node and current node as the head
        
        while curr:
            nxt = curr.next #Store in a variable
            if curr.val == val: #If value in current node == val given
                prev.next = nxt #Delete the node by pointing the previous node to the next next node
            else:
                prev = curr #If not update previous node to current node
            curr = nxt #Move current node to the next node
        return dummy.next #Return head