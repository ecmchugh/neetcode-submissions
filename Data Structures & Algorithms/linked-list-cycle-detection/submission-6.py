# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index = 0
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            index += 1
            if slow == fast:
                break
        
        if not fast or not fast.next:
            return False
        
        slow2 = head
        while slow2 != slow:
            slow = slow.next
            slow2 = slow2.next
        return True
        
