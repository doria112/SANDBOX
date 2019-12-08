class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        
        if m > n:
            transpose = [[matrix[j][i] for j in range(m)] for i in range(n)]
            matrix = transpose
            m,n = n,m
        
        for i in range(1,m):
            for l in range(n):
                matrix[i][l] += matrix[i-1][l]

        res = -float('inf')
        for j in range(m):
            for i in range(-1, j):
                pre_sums = [0]
                prev = 0
                for l in range(n):
                    row_sum = matrix[j][l] - matrix[i][l] if i > -1 else matrix[j][l]
                    col_sum = row_sum + prev
                    loc = bisect.bisect_left(pre_sums, col_sum - k)
                    if loc < len(pre_sums):
                        res = max(res, col_sum - pre_sums[loc])
                    prev = col_sum
                    bisect.insort(pre_sums, col_sum)
        return res

solution = Solution()
print(solution.maxSumSubmatrix([[1,0,1],[0,-2,3]], 2))
