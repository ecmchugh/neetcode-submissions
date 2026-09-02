# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        length = 0
        if not head.val and head.val != 0:
            return None
        while curr != None:
            length += 1
            curr = curr.next
        dif = length - n
        i, curr = 0, head
        if dif == 0:
            head = curr.next
            return head
        while i != dif:
            if i == (dif - 1):
                prev = curr
            i += 1
            curr = curr.next
        temp = curr.next
        curr.next = None
        prev.next = temp
        return head
            
            

        
        