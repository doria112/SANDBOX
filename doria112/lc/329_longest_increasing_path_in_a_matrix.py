class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        m = len(matrix)
        n = len(matrix[0])
        
        def check_out_degree(x, y, direction, m, n):
            new_x = x + direction[0]
            new_y = y + direction[1]
            if (new_x < 0) or (new_x > m-1) or (new_y < 0) or (new_y > n-1):
                return 0
            elif matrix[x][y] > matrix[new_x][new_y]:
                return 1
            else:
                return 0
            
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        out_degrees = []
        for x,row in enumerate(matrix):
            out_degree_row = []
            for y, e in enumerate(row):
                out_degree = 0
                for d in directions:
                    out_degree += check_out_degree(x,y,d,m,n)
                out_degree_row.append(out_degree)
            out_degrees.append(out_degree_row)
        leaves = []
        for x in range(m):
            for y in range(n):
                if out_degrees[x][y] == 0:
                    leaves.append([x,y])
         
        length = 0
        
        new_leaves = []
        while leaves:
            
            # reduce out_degree to each leaf's neighbor
            # if the out_degree is zero, add it into the new_leaves
            
            for leaf in leaves:
                for d in directions:
                    new_x = leaf[0] + d[0]
                    new_y = leaf[1] + d[1]
                    
                    if (new_x < 0) or (new_x > m-1) or (new_y < 0) or (new_y > n-1):
                        continue;
                    
                    if matrix[leaf[0]][leaf[1]] < matrix[new_x][new_y]: 
                        out_degrees[new_x][new_y] -= 1
                        if out_degrees[new_x][new_y] == 0:
                            new_leaves.append([new_x, new_y])
            length += 1
            leaves = new_leaves
            new_leaves = []
            
        return length

solution = Solution()
test_input1 = []
test_input2 = [[3,4,5],[3,2,6],[2,2,1]]
print(solution.longestIncreasingPath(test_input2))
