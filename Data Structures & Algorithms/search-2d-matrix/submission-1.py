class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix)*len(matrix[0])-1
        while l<=r:
            m = l + (r-l)//2
            if matrix[m//len(matrix[0])][m%len(matrix[0])] == target:
                return True
            elif matrix[m//len(matrix[0])][m%len(matrix[0])] < target:
                l = m +1
            else:
                r = m -1
        return False
