# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0 
        head = ListNode()
        curr = head
        while l1 or l2 or carry != 0:
            if l1:
                x = l1.val
            else:
                x = 0
            if l2:
                y = l2.val
            else:
                y = 0
            add = x + y + carry
            if add >= 10:
                add = add % 10
                carry = 1
                curr.val = add
            else:
                carry = 0
                curr.val = add
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next   
            if l1 or l2 or carry != 0:
                curr.next = ListNode()
                curr = curr.next
        return head
            