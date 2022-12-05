class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = [0] * n
        
        for i in range(m-1, 0, -1):
            dp_new = [0] * n
            for j in range(n): # j is target col
                for k in range(n): # k is lower row's col
                    dp_new[j] = max(dp_new[j], dp[k]+points[i][k]-abs(j-k))
            dp = dp_new

        for j in range(n):
            dp[j] += points[0][j]
            
        return max(dp)
