class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        m = {}
        path = set()
        visited = set()
        if len(pre) == 0:
            return True
        for i in range(len(pre)):
            if pre[i][0] in m:
                m[pre[i][0]].append(pre[i][1])
            else:
                m[pre[i][0]] = [pre[i][1]]
        
        def dfs(node):
            if node in path:
                return False
            if node in visited:
                return True

            path.add(node)
            for neighbor in m.get(node, []):
                if dfs(neighbor) == False:
                    return False
            path.remove(node)
            visited.add(node)
            return True


        for course in range(numCourses):
            if dfs(course) == False:
                return False
        return True
