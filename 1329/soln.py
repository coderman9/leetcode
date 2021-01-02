class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        def sort_diagonal(startR, startC):
            diagonal = [mat[startR + i][startC + i] for i in range(0, min(width - startC, height - startR))]
            diagonal.sort()
            for i in range(0, min(width - startC, height - startR)):
                mat[startR + i][startC + i] = diagonal[i]
        for i in range(width):
            sort_diagonal(0, i)
        for i in range(height):
            sort_diagonal(i, 0)
        return mat
