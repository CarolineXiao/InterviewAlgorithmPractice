class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
    
        # 1. brute force: time O(n^2)
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == target:
        #             return True
        # return False   
        
        # 2. O(m + n)
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False

        row = 0
        col = len(matrix[0]) - 1

        while (row < len(matrix) and col >= 0):
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False
