# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        head = ListNode()
        
        if list1.val <= list2.val:
            head.val = list1.val
            list1 = list1.next
        else:
            head.val = list2.val
            list2 = list2.next
        
        prev = head
        curr = head

        while (list1 and list2):
            curr = ListNode()
            if list1.val <= list2.val:
                curr.val = list1.val
                list1 = list1.next
            else:
                curr.val = list2.val
                list2 = list2.next
            prev.next = curr
            prev = curr
        
        if list1:
            curr.next = list1
            return head
        else:
            curr.next = list2
            return head



