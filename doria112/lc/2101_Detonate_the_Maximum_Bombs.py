from collections import defaultdict
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = defaultdict(list)
        for i in range(n-1):
            for j in range(i+1, n):
                dist = sqrt((bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2)
                if dist <= bombs[i][2]:
                    graph[i].append(j)
                if dist <= bombs[j][2]:
                    graph[j].append(i)
        
        def dfs(bomb, visited, graph):
            for n in graph[bomb]:
                if n in visited:
                    continue
                visited.add(n)
                dfs(n, visited, graph)

        max_count = 0
        for i, bomb in enumerate(bombs):
            visited = set([i])
            dfs(i, visited, graph)
            if len(visited) > max_count:
                max_count = len(visited) 
        
        return max_count
