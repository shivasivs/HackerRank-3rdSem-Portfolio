#!/usr/bin/env python3
"""HackerRank: Sparse Arrays."""

from collections import Counter

def matchingStrings(strings, queries):
    frequencies = Counter(strings)
    return [frequencies[query] for query in queries]

def main():
    import sys
    data = sys.stdin.buffer.read().decode().splitlines()
    if not data:
        return
    n = int(data[0])
    strings = data[1:1+n]
    q = int(data[1+n])
    queries = data[2+n:2+n+q]
    print('\n'.join(map(str, matchingStrings(strings, queries))))

if __name__ == '__main__':
    assert matchingStrings(['aba', 'baba', 'aba', 'xzxb'], ['aba', 'xzxb', 'ab']) == [2, 1, 0]
    assert matchingStrings(['x', 'x', 'y'], ['x', 'y', 'z']) == [2, 1, 0]
    main()
