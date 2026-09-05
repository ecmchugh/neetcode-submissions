# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val, None, None)
        def dfs(node):
            if not node.right and val > node.val:
                node.right = TreeNode(val, None, None)
                return
            if not node.left and val < node.val:
                node.left = TreeNode(val, None, None)
                return
            if node.right and val > node.val:
                dfs(node.right)
            if node.left and val < node.val:
                dfs(node.left)
        dfs(root)
        return root