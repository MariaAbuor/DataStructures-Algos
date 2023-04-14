# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#Using Two-Pointer Method
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head #Both pointers start at the same position
        
        while fast and fast.next:#if fast and fast.next is not null
            slow = slow.next #Slow pointer moves one step
            fast = fast.next.next #Fast pointer moves two steps
            if fast == slow: #If they meet, then there is a cycle
                return True
        return False