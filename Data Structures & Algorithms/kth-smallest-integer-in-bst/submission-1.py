# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        self.temp = 0
        if root is None: return 0
        def findSmallest(root, k):
            if root is None: return 0
            findSmallest(root.left, k)
            self.i += 1
            if self.i == k:
                self.temp = root.val
            findSmallest(root.right, k)  
        findSmallest(root, k)
        return self.temp
