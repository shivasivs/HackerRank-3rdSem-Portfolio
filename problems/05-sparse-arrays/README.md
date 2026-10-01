# Sparse Arrays

**HackerRank domain:** Data Structures / Strings  
**Function:** `matchingStrings(strings, queries)`

## Approach

Build a frequency map from the input strings once. For each query, look up its count and return the results in query order.

## Complexity

- Time: O(total input characters + total query characters) expected, using a hash map. This is O(N + Q) when string lengths are bounded.
- Extra space: O(N) distinct stored strings.

## Notes

String matching is exact and case-sensitive. A missing key returns zero.

## Practice cases

1. `['aba', 'baba', 'aba', 'xzxb']`, queries `['aba', 'xzxb', 'ab']` -> `[2, 1, 0]`
2. `['x', 'x', 'y']`, queries `['x', 'y', 'z']` -> `[2, 1, 0]`
