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

'''
Add 
'''
from collections import defaultdict

class Solution2(object):
    def criticalConnections(self, n, connections):
        
        graph = defaultdict(list)
        
        for connection in connections:
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])
        
        disc = [None for _ in range(n)]
        low = [None for _ in range(n)]
        res = []
        self.cur = 0
        
        def dfs(node, parent):
            if disc[node] is None:
                disc[node] = self.cur
                low[node] = self.cur
                self.cur += 1
                for n in graph[node]:
                    dfs(n, node)
                for n in graph[node]:
                    if low[n] < low[node] and n!=parent:
                        low[node] = low[n]
        
        dfs(0, None)
        
        for connection in connections:
            if low[connection[0]] > disc[connection[1]] or low[connection[1]] > disc[connection[0]]:
                res.append(connection)
        
        return res    