1329 Sort the Matrix Diagonally
---
__Difficulty:__ Medium

Description
---
A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

Solution
---
Can get all the diagonals by looking at those that start at (0, x) and (y, 0) for all x, y in the appropriate range. Then sorting them is just a question of collecting the elements, sorting that list, then iterating through the diagonal again to insert.