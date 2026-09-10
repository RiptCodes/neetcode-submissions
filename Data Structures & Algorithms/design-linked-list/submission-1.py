# ListNode defined as I need to use a dummy for the head and tail to make insertion and deletion easier
class ListNode():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)
        self.tail = ListNode(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
# Defining current node as head.next
    def get(self, index: int) -> int: 
        if index < 0:
            return -1
    
        curr = self.head.next 
        for _ in range(index): 
            if curr == self.tail:
                return -1
            # for loop with "_" to show that we are just going along the index with no need to put the indecies and looping from 0-index.
            curr = curr.next # self.head.next.next going to go to the next node 
        if curr == self.tail:
            return -1
        return curr.val

        

    def addAtHead(self, val: int) -> None:
        node, next, prev = ListNode(val), self.head.next, self.head
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
  


    def addAtTail(self, val: int) -> None:
        node, tail, prev = ListNode(val), self.tail, self.tail.prev
        prev.next = node
        tail.prev = node
        node.next = tail
        node.prev = prev
        

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        node, next_node, prev = ListNode(val), curr.next, curr
        prev.next = node
        next_node.prev = node
        node.next = next_node
        node.prev = prev

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head
        for _ in range(index):
            curr = curr.next
        
        if curr.next != self.tail:
            node_to_delete = curr.next
            next_node = node_to_delete.next
            
            curr.next = next_node
            next_node.prev = curr

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)