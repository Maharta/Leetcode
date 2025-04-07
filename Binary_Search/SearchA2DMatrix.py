class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t = 0
        b = len(matrix) - 1

        while (t <= b):
            matrixMiddle = (t + b) // 2
            lst = matrix[matrixMiddle]

            if lst[0] <= target <= lst[-1]:
                l = 0
                r = len(lst) - 1

                while (l <= r):
                    m = (l + r) // 2
                    if lst[m] == target:
                        return True
                    elif lst[m] < target:
                        l = m + 1
                    else:
                        r = m - 1
            if target < lst[0]:
                b = matrixMiddle - 1
            else:
                t = matrixMiddle + 1

        return False
