from collections import defaultdict
from collections import deque
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        ans = 0
        in_degree = [0] * n
        graph = defaultdict(list)
        for r in relations:
            graph[r[0]].append(r[1])
            in_degree[r[1]-1] += 1 #assume no duplicated edge
        
        completed = 0
        taken_c = deque()
        for i, d in enumerate(in_degree):
            if d == 0:
                taken_c.append(i+1)
        while taken_c:
            new_taken_c = deque()
            completed += len(taken_c)
            for c in taken_c:
                for nc in graph[c]:
                    in_degree[nc-1] -= 1
                    if in_degree[nc-1] == 0:
                        new_taken_c.append(nc)
            taken_c = new_taken_c
            ans += 1
        if completed != n:
            return -1
        return ans
