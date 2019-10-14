'''
1st approach: DFS
Time limit exceeded with large input
'''
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(connections)):
            remove_connection = connections.pop(i)
            visited = [False] * n
            
            def dfs(node):
                visited[node] = True
                for i in range(n):
                    if not visited[i] and ([node,i] in connections or [i,node] in connections):
                        dfs(i)
            dfs(0)
            for node in visited:
                if not node:
                    res.append(remove_connection)
                    break
            connections.insert(i,remove_connection)
        return res