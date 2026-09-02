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
            leftHeight = height(root.left)
            rightHeight = height(root.right)
            if abs(leftHeight - rightHeight) > 1:
                return -float("inf")
            else:
                return 1 + max(rightHeight, leftHeight)
        
        if height(root) == -float("inf"):
            return False
        else:
            return True