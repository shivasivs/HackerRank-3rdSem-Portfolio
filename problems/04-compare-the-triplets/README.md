# Compare the Triplets

**HackerRank domain:** Algorithms / Implementation  
**Function:** `compareTriplets(a, b)`

## Approach

Compare the two scores at each of the three positions. Award one point to Alice when her value is larger and one to Bob when his value is larger. Equal values award no points.

## Complexity

- Time: O(1), because there are exactly three comparisons.
- Extra space: O(1).

## Notes

The result is returned as `[Alice score, Bob score]`, matching the HackerRank interface.

## Practice cases

1. `[5, 6, 7]` vs `[3, 6, 10]` -> `[1, 1]`
2. `[17, 28, 30]` vs `[99, 16, 8]` -> `[2, 1]`
