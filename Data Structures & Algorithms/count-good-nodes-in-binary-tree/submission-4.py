# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, maximum=-100) -> int:
        if root is None:
            return 0
        if root.val >= maximum:
            maximum = root.val
            return 1 + self.goodNodes(root.left, maximum) + self.goodNodes(root.right, maximum)
        else:
            return self.goodNodes(root.left, maximum) + self.goodNodes(root.right, maximum)
