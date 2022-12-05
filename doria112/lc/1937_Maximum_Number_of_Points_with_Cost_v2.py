class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])
        dp = points[0]
        
        for i in range(1, m):
            left_max, right_max = -float('inf'), -float('inf')
            dp_left, dp_right = [0]*n, [0]*n
            for j in range(n):
                left_max = max(left_max, dp[j]+j)
                dp_left[j]= left_max-j+points[i][j]
            for j in range(n-1, -1, -1):
                right_max = max(right_max, dp[j]-j)
                dp_right[j] = right_max+j+points[i][j]
            dp = [max(dp_left[j], dp_right[j]) for j in range(n)]
        return max(dp)
