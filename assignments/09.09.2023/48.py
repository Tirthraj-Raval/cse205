class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        x = 0
        y = len(matrix) - 1

        while x<y:
            matrix[x], matrix[y] = matrix[y], matrix[x]
            x += 1
            y -= 1
            
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]  
         

        