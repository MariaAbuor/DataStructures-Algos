class ListNode:
    def __init__ (self, val):
        self.val = val
        self.prev = None
        self.next = None
class MyLinkedList:

    def __init__(self):
        #Initialize dummy nodes left and right
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        #Cur node is after the left dummy node
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        #Check if cur is not null, and is not the last dummy node, and the index is zero
        if cur and cur != self.right and index == 0:
            return cur.val
        return -1
    
    def addAtHead(self, val: int) -> None:
        node, next, prev, = ListNode(val), self.left.next, self.left
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtTail(self, val: int) -> None:
        node, next, prev, = ListNode(val), self.right, self.right.prev
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            #Create node, next pointer, and previous pointer
            node, next, prev, = ListNode(val), cur, cur.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev


    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        #Check if cur is not null, and is not the last dummy node, and the index is zero
        if cur and cur != self.right and index == 0:
            next, prev, = cur.next, cur.prev
            prev.next = next
            next.prev = prev
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)