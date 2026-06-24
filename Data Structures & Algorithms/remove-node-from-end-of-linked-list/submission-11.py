# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        count = 1

        if not head.next and n == 1:
            return None

        while (fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            count += 2
        if fast.next:
            count += 1
        
        pos = count - n
        
        if pos == 0:
            return head.next

        if pos <= count // 2:
            curr = head
            for i in range(pos-1):
                curr = curr.next
            curr.next = curr.next.next
        else:
            pos = pos - (count-1) // 2
            print(slow.val)
            print(pos)
            if pos == 0:
                slow.next = slow.next.next
            else:
                curr = slow
                for i in range(pos-1):
                    curr = curr.next
                curr.next = curr.next.next
        return head
            

        