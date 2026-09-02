# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkSubTree( root, subRoot):
            if root is None and subRoot is None:
                return True
            if root is None and subRoot is not None:
                return False
            if root is not None and subRoot is None:
                return False
            curr = root.val
            sub = subRoot.val
            if curr == sub:
                return checkSubTree(root.left, subRoot.left) and checkSubTree(root.right, subRoot.right)
            else:
                return False
        
        if root is None:
            return False
        
        if checkSubTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
                
                
        