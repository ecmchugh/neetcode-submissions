# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        head = ListNode(0)
        current = head
        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                current = current.next
                l1 = l1.next
            elif l1.val > l2.val:
                current.next = l2
                current = current.next
                l2 = l2.next
        if l1 == None:
            current.next = l2
        elif l2 == None:
            current.next = l1
        return head.next

        