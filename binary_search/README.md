# Binary Search

This folder contains my practice problems related to Binary Search.

## Concepts

* Binary Search
* Sorted Arrays
* Left and Right Pointers
* Middle Index
* Search Space Reduction
* Finding Boundaries
* Time and Space Complexity

## Problems

| Problem | Approach | Time | Space |
|---|---|---|---|
| Binary Search | Binary Search | O(log n) | O(1) |
| Search Insert Position | Binary Search | O(log n) | O(1) |
| Guess Number Higher or Lower | Binary Search | O(log n) | O(1) |
| First Bad Version | Binary Search | O(log n) | O(1) |
| Sqrt(x) | Binary Search | O(log n) | O(1) |

## Binary Search Pattern

The basic binary search pattern used in these problems:

```text
left = 0
right = n - 1

while left <= right:

    mid = (left + right) // 2

    if target == nums[mid]:
        return mid

    elif target > nums[mid]:
        left = mid + 1

    else:
        right = mid - 1