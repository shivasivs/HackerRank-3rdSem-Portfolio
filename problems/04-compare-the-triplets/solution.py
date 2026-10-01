#!/usr/bin/env python3
"""HackerRank: Compare the Triplets."""

def compareTriplets(a, b):
    alice = sum(left > right for left, right in zip(a, b))
    bob = sum(left < right for left, right in zip(a, b))
    return [alice, bob]

def main():
    import sys
    values = list(map(int, sys.stdin.buffer.read().split()))
    if len(values) >= 6:
        print(*compareTriplets(values[:3], values[3:6]))

if __name__ == '__main__':
    assert compareTriplets([5, 6, 7], [3, 6, 10]) == [1, 1]
    assert compareTriplets([17, 28, 30], [99, 16, 8]) == [2, 1]
    main()
