# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if root is None:
                return 0
            if abs(height(root.left) - height(root.right)) > 1:
                return -float("inf")
            else:
                return 1 + max(height(root.left), height(root.right))
        
        if height(root) == -float("inf"):
            return False
        else:
            return True