class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        m = {}
        count = 0
        totalCount = 0
        self.nodeCount = 0
        for i in range(len(edges)):
            if edges[i][0] in m:
                m[edges[i][0]].append(edges[i][1])
            else:
                m[edges[i][0]] = [edges[i][1]]
            if edges[i][1] in m:
                m[edges[i][1]].append(edges[i][0])
            else:
                m[edges[i][1]] = [edges[i][0]]

        def dfs(node):
            if node in visit:
                return True
            visit.add(node)
            self.nodeCount += 1
            for neighbor in m.get(node, []):
                if neighbor in visit:
                    continue
                else:
                    dfs(neighbor)
            return True
        
        for i in range(n):
            if i not in visit and dfs(i) == True:
                count += 1
                totalCount += self.nodeCount
                self.nodeCount = 0
        if totalCount == n:
            return count
            
            





