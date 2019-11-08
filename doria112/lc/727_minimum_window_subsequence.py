class Solution:
    def minWindow(self, S: str, T: str) -> str:
        if len(T) == 0:
            return ''
        shortest = [0] * len(S)
        for i,t in enumerate(T):
            new_shortest = [None] * len(S)
            for j,s in enumerate(S):
                if s == t:
                    # look for the previous position in S that ending previous t
                    if i == 0:
                        new_shortest[j] = 1
                    elif j > 0 and shortest[j-1]:
                        new_shortest[j] = shortest[j-1] + 1
                elif j > 0 and new_shortest[j-1]:
                    new_shortest[j] = new_shortest[j-1] + 1
            shortest = new_shortest
        min_window = -1
        min_index = len(S)        
        for i,l in enumerate(shortest):
            if l and (l < min_window or min_window == -1):
                min_index = i
                min_window = l
        return S[min_index - min_window+1: min_index+1] if min_window != -1 else ''

solution = Solution()
print(solution.minWindow('abcdebdde', 'bde'))
print(solution.minWindow('', ''))
print(solution.minWindow('sdf', 'a'))
