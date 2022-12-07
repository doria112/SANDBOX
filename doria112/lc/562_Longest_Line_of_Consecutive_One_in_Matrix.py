class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        dp = [[[0 for _ in range(4)] for _ in range(n+1)] for _ in range(m+1)]
 
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    dp[i+1][j+1][0] = dp[i][j+1][0]+1
                    dp[i+1][j+1][1] = dp[i+1][j][1]+1
                    dp[i+1][j+1][2] = dp[i][j][2]+1
                    if j+2 < n+1:
                        dp[i+1][j+1][3] = dp[i][j+2][3]+1

        return max(dp[i][j][k] for i in range(1, m+1) for j in range(1, n+1) for k in range(4))
