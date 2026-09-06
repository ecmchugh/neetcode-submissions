# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        curr = head
        m = {}
        while curr: 
            if curr.val in m:
                m[curr.val] = True
            else:
                m[curr.val] = False
            curr = curr.next
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        while curr:
            if m[curr.val]:
                temp = curr.next
                curr.next = None
                prev.next = temp
                curr = temp
            else:
                prev = curr
                curr = curr.next
        return dummy.next
