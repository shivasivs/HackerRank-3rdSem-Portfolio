# Time Conversion

**HackerRank domain:** Strings  
**Function:** `timeConversion(s)`

## Approach

Separate the six-character clock value from the AM/PM suffix. Convert only the hour: midnight (`12 AM`) becomes `00`, noon (`12 PM`) stays `12`, and other PM hours increase by 12. Preserve minutes and seconds exactly.

## Complexity

- Time: O(1), because the input has a fixed length.
- Extra space: O(1).

## Notes

The hour is zero-padded to two digits. This covers the two boundary cases that often cause mistakes: midnight and noon.

## Practice cases

1. `07:05:45PM` -> `19:05:45`
2. `12:00:00AM` -> `00:00:00`
3. `12:00:00PM` -> `12:00:00`
