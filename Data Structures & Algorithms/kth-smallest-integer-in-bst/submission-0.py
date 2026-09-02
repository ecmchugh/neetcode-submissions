# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0
        self.heap = []
        def findSmallest(root, k):
            if root is None:
                return 0
            findSmallest(root.left, k)
            findSmallest(root.right, k)
            heapq.heappush(self.heap, root.val)
        findSmallest(root, k)
        for i in range(k):
            temp = heapq.heappop(self.heap)
        return temp