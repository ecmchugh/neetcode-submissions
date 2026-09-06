# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0, head)
        counter = 1
        prev = dummy
        curr = head
        while curr:
            if counter == left:
                start = prev
                startHead = curr
                prev = curr
                curr = curr.next
                counter += 1
                break
            prev = curr
            curr = curr.next
            counter += 1
        while counter <= right:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            counter += 1
        startHead.next = curr
        start.next = prev
        return dummy.next

            