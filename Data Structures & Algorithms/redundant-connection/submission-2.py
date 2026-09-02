class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(len(edges)):
            if edges[i][0] in adj:
                adj[edges[i][0]].append(edges[i][1])
            else:
                adj[edges[i][0]] = [edges[i][1]]
            if edges[i][1] in adj:
                adj[edges[i][1]].append(edges[i][0])
            else:
                adj[edges[i][1]] = [edges[i][0]]
        visited = set()
        def dfs(node, parent, visited):
            visited.add(node)
            for neighbor in adj.get(node, []):
                if neighbor not in visited:
                    if dfs(neighbor, node, visited):
                        return True
                elif neighbor != parent:
                    return True
                    
            return False

        for i in range(len(edges) - 1, -1, -1):
            adj[edges[i][0]].remove(edges[i][1])
            adj[edges[i][1]].remove(edges[i][0])
            a = dfs(edges[i][0], None, set())
            b = dfs(edges[i][1], None, set())
            adj[edges[i][0]].append(edges[i][1])
            adj[edges[i][1]].append(edges[i][0])
            if a or b:
                continue
            else:
                return edges[i]
