# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None and q:
            return False
        elif p and q is None:
            return False

        q1 = deque()
        q2 = deque()
        q1.append(p)
        q2.append(q)


        while q1 and q2:
            if len(q1) != len(q2):
                return False
            temp1 = q1.popleft()
            temp2 = q2.popleft()
            if (temp1.left and temp2.left is None) or (temp2.left and temp1.left is None):
                return False
            if (temp1.right and temp2.right is None) or (temp2.right and temp1.right is None):
                return False
            if temp1.val != temp2.val:
                return False
            if temp1.left is not None:
                q1.append(temp1.left)
            if temp1.right is not None:
                q1.append(temp1.right)
            if temp2.left is not None:
                q2.append(temp2.left)
            if temp2.right is not None:
                q2.append(temp2.right)
        return True
                
            
            


