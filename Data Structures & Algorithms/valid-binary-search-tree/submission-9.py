# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], minimum = float('-inf'), maximum = float('inf')) -> bool:
        if root is None:
            return True
        if root.val >= maximum or root.val <= minimum:
            return False
        if self.isValidBST(root.left, minimum, maximum = root.val) and self.isValidBST(root.right, minimum = root.val, maximum = maximum):
            return True
        else:
            return False

