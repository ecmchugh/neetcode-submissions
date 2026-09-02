# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head, head
        index = 0
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            index+=1
            if slow == fast:
                break
        if not fast or not fast.next:
            index = -1
            return False

        return True
        
        
