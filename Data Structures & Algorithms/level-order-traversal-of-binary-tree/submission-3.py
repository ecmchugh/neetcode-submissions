# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        queue = deque()
        queue.append(root)
        current = []
        while queue:
            for i in range(len(queue)):
                temp = queue.popleft()
                if temp is None:
                    continue
                queue.append(temp.left)
                queue.append(temp.right)
                
                current.append(temp.val)
            if current:
                ans.append(current)
                current = []
        return ans
                

        