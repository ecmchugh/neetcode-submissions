# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0 
        
        def height(root):
            if root is None:
                return 0

            left_height = height(root.left)
            right_height = height(root.right)

            self.diameter = max(self.diameter, left_height + right_height)

            return 1 + max(left_height, right_height)
        
        height(root)
        return self.diameter
        

            


