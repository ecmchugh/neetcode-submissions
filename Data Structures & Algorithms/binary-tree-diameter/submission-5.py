# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        self.maximum = 0
        def height(root):
            if root is None: return 0
            return 1 + max(height(root.left), height(root.right))
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        total = height(root.left) + height(root.right)
        self.maximum = max(self.maximum, total)
        
        return self.maximum

        
        

            


