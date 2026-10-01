# Diagonal Difference

**HackerRank domain:** 2D Arrays  
**Function:** `diagonalDifference(arr)`

## Approach

Traverse the square matrix once. At each row index `i`, add `arr[i][i]` to the primary diagonal and `arr[i][n - 1 - i]` to the secondary diagonal. Return the absolute difference of the sums.

## Complexity

- Time: O(N), for an N by N matrix.
- Extra space: O(1).

## Notes

This handles odd and even dimensions, negative values, and the 1-by-1 case. The main function reads the HackerRank input format.

## Practice cases

1. `[[11, 2, 4], [4, 5, 6], [10, 8, -12]]` -> `15`
2. `[[1]]` -> `0`
