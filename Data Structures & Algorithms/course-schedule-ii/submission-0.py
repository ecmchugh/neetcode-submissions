class Solution:
    def findOrder(self, n: int, pre: List[List[int]]) -> List[int]:
        visit = set()
        currentPath = []
        path = set()
        m = {}
        
        for i in range(len(pre)):
            if pre[i][0] in m:
                m[pre[i][0]].append(pre[i][1])
            else:
                m[pre[i][0]] = [pre[i][1]]
        
        def dfs(node):
            if node in path:
                return False
            if node in visit:
                return True
            path.add(node)
            for neighbor in m.get(node, []):
                if dfs(neighbor) == False:
                    return False
            path.remove(node)
            visit.add(node)
            currentPath.append(node)
            return currentPath

        for i in range(n):
            if dfs(i) == False:
                return []
        return currentPath
