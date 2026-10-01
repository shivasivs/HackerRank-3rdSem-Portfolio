# Dynamic Array

**HackerRank domain:** Data Structures  
**Function:** `dynamicArray(n, queries)`

## Approach

Create `n` empty lists and initialize `last_answer` to zero. For every query, calculate `(x XOR last_answer) % n`. Type 1 appends `y` to the selected list. Type 2 selects the element at `y % len(list)`, updates `last_answer`, and records it.

## Complexity

- Time: O(Q) amortized for Q queries, plus the total cost of list growth; O(N + Q) including initialization.
- Extra space: O(N + Q) in the worst case for stored values and returned answers.

## Notes

The selected sequence for a type-2 query is guaranteed by the challenge to be non-empty. XOR is written as `^` in Python.

## Practice cases

1. The standard 2-sequence example returns `[7, 3]`.
2. With `n=1`, append 9 then query index 0; output is `[9]`.
