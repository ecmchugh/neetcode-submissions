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
            if not l1:
                x = 0
            else:
                x = l1.val
            if not l2:
                y = 0 
            else:
                y = l2.val
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
            if l2 != None or l1 != None or carry != 0:
                curr.next = ListNode()
                curr = curr.next
        return head
