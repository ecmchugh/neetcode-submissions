"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
import copy
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        clones = {}
        head = Node(node.val)
        head.val = node.val
        original_queue = deque()
        original_queue.append(node)
        new_queue = deque()
        new_queue.append(head)
        clones[node] = head
        visit = set()
        visit.add(node)

        while original_queue:
            original = original_queue.popleft()
            new = new_queue.popleft()
            for neighbor in original.neighbors:
                if neighbor not in visit:
                    temp = Node(node.val)
                    temp.val = neighbor.val
                    visit.add(neighbor)
                    original_queue.append(neighbor)
                    new_queue.append(temp)
                    new.neighbors.append(temp)
                    clones[neighbor] = temp
                else:
                    new.neighbors.append(clones[neighbor])
                    continue

        return head