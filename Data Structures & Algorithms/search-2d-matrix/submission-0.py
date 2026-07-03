class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        while l <= r:
            mid = (l + r) // 2
            row = mid // cols
            col = mid % cols
            val = matrix[row][col]
            if target > val:
                l = mid + 1
            elif target < val:
                r = mid - 1
            else:
                return True
        return False