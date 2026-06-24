# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head

        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
        
        l1 = head
        l2 = slow.next
        slow.next = None
        

        prev = None
        curr = l2
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            l2 = curr
            curr = temp
        

        dummy = ListNode()
        curr = dummy
        
        while (l1 and l2):
            curr.next = l1
            l1 = l1.next
            curr = curr.next
            curr.next = l2
            l2 = l2.next
            curr = curr.next
            
        
        if l1:
            curr.next = l1
        
        head = dummy.next

        

        






        