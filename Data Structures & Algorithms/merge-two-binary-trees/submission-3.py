# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 and not root2:
            return root1
        if root2 and not root1:
            return root2
        if root2 is None and root1 is None:
            return None
        head = root2
        def dfs(root1, root2):
            root2.val = root2.val + root1.val
            if root1.right and root2.right:
                dfs(root1.right, root2.right)
            if root1.left and root2.left:
                dfs(root1.left, root2.left)
            if root1.left and not root2.left:
                root2.left = root1.left
            if root1.right and not root2.right:
                root2.right = root1.right
        dfs(root1, root2)
        return head

