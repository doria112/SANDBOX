class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = collections.defaultdict(list)
        # create the graph
        for n1, n2, d in times:
            graph[n1].append((n2, d))
        dist = [float('inf')] * N
        visited = set()
        dist[K-1] = 0
        cur = K
        while True:
            for n, d in graph[cur]:
                dist[n-1] = min(dist[n-1], dist[cur-1] + d)
            visited.add(cur)
            
            # find the next shortest distance
            cur = -1
            min_dist = float('inf')
            for n in range(1, N+1):
                if n not in visited and dist[n-1] < min_dist:
                    cur = n
                    min_dist = dist[n-1]
            if cur == -1:
                break
        max_dist = max(dist)
        return -1 if len(visited) < N else max_dist 
    
solution = Solution()
test1 = [[2,1,1],[2,3,1],[3,4,1]]
print(solution.networkDelayTime(test1, 4, 2))
