class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        
        result = [[1], [1, 1]]
        
        for i in range(2, numRows):
            newRow = [1]
            prevRow = result[-1]
            for j in range(1, i):
                newRow.append(prevRow[j - 1] + prevRow[j])
            newRow.append(1)
            result.append(newRow)
        
        return result
