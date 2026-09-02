class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        path = set()
        visited = set()
        m = {}
        cameFrom = None
        if not len(edges) == n - 1:
            return False
        for i in range(len(edges)):
            if edges[i][0] in m:
                m[edges[i][0]].append(edges[i][1])
            else:
                m[edges[i][0]] = [edges[i][1]]
            if edges[i][1] in m:
                m[edges[i][1]].append(edges[i][0])
            else:
                m[edges[i][1]] = [edges[i][0]]
        
        def dfs(node, parent):
            if node in path:
                return False
            if node in visited:
                return True
            path.add(node)
            for neighbor in m.get(node, []):
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            path.remove(node)
            visited.add(node)
            return True
        
        for i in range(n):
            if not dfs(i, -1):
                return False
        return True
        