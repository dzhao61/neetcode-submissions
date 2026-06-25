# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        start = ListNode()
        prev = start
        cf = 0

        while l1 and l2:
            curr = ListNode()
            prev.next = curr
            
            i = l1.val + l2.val + cf
            curr.val =  i % 10 
            cf = i // 10 
            
            l1 = l1.next
            l2 = l2.next
            prev = prev.next
        
        while l1:
            curr = ListNode()
            prev.next = curr
            
            i = l1.val + cf
            curr.val =  i % 10 
            cf = i // 10 
            
            l1 = l1.next
            prev = prev.next
        
        while l2:
            curr = ListNode()
            prev.next = curr
            
            i = l2.val + cf
            curr.val =  i % 10 
            cf = i // 10 
            
            l2 = l2.next
            prev = prev.next

        if cf:
            curr = ListNode()
            prev.next = curr
            curr.val = cf
            curr.next = None
        else:
            prev.next = None

        return start.next










