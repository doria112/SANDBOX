class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        # convert the matrices to non-zero values only 
        # first matrix keyed by row, second matrix keyed by column
        m = len(mat1)
        k = len(mat1[0])
        n = len(mat2[0])

        # compress mat1
        nz1, col1, row1 = [], [], [0]
        for row in mat1:
            for col, ele in enumerate(row):
                if ele != 0:
                    nz1.append(ele)
                    col1.append(col)
            row1.append(len(nz1))
        print(nz1, row1, col1)
            
        # compress mat2
        nz2, row2, col2 = [], [], [0]
        for col in range(n):
            for row in range(k):
                ele = mat2[row][col]
                if ele != 0:
                    nz2.append(ele)
                    row2.append(row)
            col2.append(len(nz2))
        print(nz2, row2, col2)
        
        
        rv = [[0]*n for _ in range(m)]
        # fill in rv
        for i in range(m):
            row_indices = col1[row1[i]:row1[i+1]]
            row_value = nz1[row1[i]:row1[i+1]]
            for j in range(n):
                col_indices = row2[col2[j]:col2[j+1]]
                col_value = nz2[col2[j]:col2[j+1]]
                pt1, pt2 = 0, 0
                while pt1 < len(row_indices) and pt2 < len(col_indices):
                    if row_indices[pt1] == col_indices[pt2]:
                        rv[i][j] += row_value[pt1]*col_value[pt2]
                        pt1 += 1
                        pt2 += 1
                    elif row_indices[pt1] <= col_indices[pt2]:
                        pt1 += 1
                    else:
                        pt2 += 1
                        
        return rv
