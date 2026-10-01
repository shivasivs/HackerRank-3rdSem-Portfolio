#!/usr/bin/env python3
"""HackerRank: Diagonal Difference."""

def diagonalDifference(arr):
    n = len(arr)
    primary = sum(arr[i][i] for i in range(n))
    secondary = sum(arr[i][n - 1 - i] for i in range(n))
    return abs(primary - secondary)

def main():
    import sys
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n = data[0]
    arr = [data[1 + i*n:1 + (i+1)*n] for i in range(n)]
    print(diagonalDifference(arr))

if __name__ == '__main__':
    assert diagonalDifference([[11, 2, 4], [4, 5, 6], [10, 8, -12]]) == 15
    assert diagonalDifference([[1]]) == 0
    main()
