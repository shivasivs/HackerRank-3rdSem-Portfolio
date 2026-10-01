#!/usr/bin/env python3
"""HackerRank: Dynamic Array."""

def dynamicArray(n, queries):
    sequences = [[] for _ in range(n)]
    last_answer = 0
    answers = []
    for query_type, x, y in queries:
        index = (x ^ last_answer) % n
        if query_type == 1:
            sequences[index].append(y)
        else:
            sequence = sequences[index]
            last_answer = sequence[y % len(sequence)]
            answers.append(last_answer)
    return answers

def main():
    import sys
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    n, q = data[:2]
    queries = [data[2 + 3*i:5 + 3*i] for i in range(q)]
    print('\n'.join(map(str, dynamicArray(n, queries))))

if __name__ == '__main__':
    assert dynamicArray(2, [[1, 0, 5], [1, 1, 7], [1, 0, 3], [2, 1, 0], [2, 1, 1]]) == [7, 3]
    assert dynamicArray(1, [[1, 0, 9], [2, 0, 0]]) == [9]
    main()
