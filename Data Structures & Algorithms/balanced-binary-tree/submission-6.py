# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.difference = 0
        self.balanced = None
        def height(root):
            if root is None:
                return 0
            lheight = height(root.left)
            rheight = height(root.right)
            self.difference = abs(rheight-lheight)
            if self.difference > 1:
                self.balanced = False
            return 1 + max(lheight,rheight)
        height(root)
        if self.balanced != False:
            return True
        else:
            return False