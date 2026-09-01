# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # [3, 6]

        if not head: # not empty so dont return null move to recursive
            return None

        newHead = head #temp storage of newHead at node
        if head.next: 
            # Step 1: 6.next = 3 so not Null as we swapped pointer
            # Step 2: 3.next = Null so head.next = Null 
            # Step 3: Output head recursively so [6, 3, Null]
            newHead = self.reverseList(head.next) 
            head.next.next = head
        head.next = None

        return newHead









        # prev, curr = None, head
       
        # while curr:
        #     nxt = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = nxt
        # return prev

