# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # solution: make a new dummy list that tracks the iteration of list1 and list2. Find the smallest in both lists and then add them to the dummy list in order of size. so [1, 2, 4] 1 is the smallest and [1, 3, 5] 1 is the smallest. 1 <= 1 so implement list1(1) first then list2(1) or head of both lists into dummy list. keep going until null


        dummy = ListNode(0) # created dummy
        tail = dummy # tail equal to head of dummy
        

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
        
        return dummy.next
        
            


        