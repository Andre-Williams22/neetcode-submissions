class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # get the matrix dimensions 
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2 
            # Map 1D index to 2D 
            row, col = divmod(mid, n)
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                left = mid + 1 
            else:
                right = mid - 1
        
        return False  