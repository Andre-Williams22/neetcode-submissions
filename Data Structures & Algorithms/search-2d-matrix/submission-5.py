class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for i in range(len(matrix)):
            array = matrix[i]
            l, r = 0, len(array)-1 

            while l <= r:
                mid = (l+r) // 2 
                if array[mid] == target:
                    return True 
                elif array[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1 
        
        return False 
