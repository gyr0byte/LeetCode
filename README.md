# LeetCode Python Solutions

<!-- BADGES_START -->

![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)
![Solved](https://img.shields.io/badge/Solved-52-2ea44f)
![Easy](https://img.shields.io/badge/Easy-42-6ab04c)
![Medium](https://img.shields.io/badge/Medium-8-f39c12)
![Hard](https://img.shields.io/badge/Hard-2-e74c3c)
![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--04--25-0366d6)

<!-- BADGES_END -->

A curated collection of my LeetCode solutions in Python, organized by difficulty.

## Overview

This repository contains concise and interview-focused implementations for LeetCode problems.

- Language: Python
- Total solved: 52
- Difficulty split:
  - Easy: 42
  - Medium: 8
  - Hard: 2

## Repository Structure

```text
LeetCode/
|-- EasyQuestions/
|   |-- 1.py
|   |-- 13.py
|   |-- 26.py
|   |-- 27.py
|   |-- 28.py
|   |-- 66.py
|   |-- 58.py
|   |-- 9.py
|   |-- 104.py
|   |-- 111.py
|   |-- 125.py
|   |-- 1266.py
|   |-- 1365.py
|   |-- 1672.py
|   |-- 1684.py
|   |-- 169.py
|   |-- 1979.py
|   |-- 1929.py
|   |-- 2011.py
|   |-- 217.py
|   |-- 2235.py
|   |-- 231.py
|   |-- 2413.py
|   |-- 242.py
|   |-- 2469.py
|   |-- 2496.py
|   |-- 3894.py
|   |-- 268.py
|   |-- 2769.py
|   |-- 2798.py
|   |-- 283.py
|   |-- 2894.py
|   |-- 2942.py
|   |-- 326.py
|   |-- 3274.py
|   |-- 3498.py
|   |-- 3516.py
|   |-- 3701.py
|   |-- 3110.py
|   |-- 3190.py
|   |-- 448.py
|   `-- 771.py
|-- MediumQuestions/
|   |-- 1143.py
|   |-- 238.py
|   |-- 34.py
|   |-- 49.py
|   |-- 72.py
|   |-- 75.py
|   |-- 98.py
|   `-- 153.py
`-- HardQuestions/
    |-- 4.py
    `-- 42.py
```

## Solved Problems

<!-- SOLVED_TABLE_START -->

| #    | Problem                                                         | Difficulty | File                                               | Approach                                       | Time              | Space    |
| ---- | --------------------------------------------------------------- | ---------- | -------------------------------------------------- | ---------------------------------------------- | ----------------- | -------- |
| 1    | Two Sum                                                         | Easy       | [EasyQuestions/1.py](EasyQuestions/1.py)           | One-pass hash map                              | O(n)              | O(n)     |
| 13   | Roman to Integer                                                | Easy       | [EasyQuestions/13.py](EasyQuestions/13.py)         | Left-to-right numeral comparison               | O(n)              | O(1)     |
| 26   | Remove Duplicates from Sorted Array                             | Easy       | [EasyQuestions/26.py](EasyQuestions/26.py)         | Two-pointer overwrite                          | O(n)              | O(1)     |
| 27   | Remove Element                                                  | Easy       | [EasyQuestions/27.py](EasyQuestions/27.py)         | Write-pointer compaction                       | O(n)              | O(1)     |
| 28   | Find the Index of the First Occurrence in a String              | Easy       | [EasyQuestions/28.py](EasyQuestions/28.py)         | Built-in substring search                      | O(n\*m)           | O(1)     |
| 66   | Plus One                                                        | Easy       | [EasyQuestions/66.py](EasyQuestions/66.py)         | Right-to-left carry handling                   | O(n)              | O(1)     |
| 58   | Length of Last Word                                             | Easy       | [EasyQuestions/58.py](EasyQuestions/58.py)         | Strip and split string                         | O(n)              | O(n)     |
| 9    | Palindrome Number                                               | Easy       | [EasyQuestions/9.py](EasyQuestions/9.py)           | Reverse integer and compare                    | O(log n)          | O(1)     |
| 104  | Maximum Depth of Binary Tree                                    | Easy       | [EasyQuestions/104.py](EasyQuestions/104.py)       | DFS recursion                                  | O(n)              | O(h)     |
| 111  | Minimum Depth of Binary Tree                                    | Easy       | [EasyQuestions/111.py](EasyQuestions/111.py)       | DFS recursion with null-child handling         | O(n)              | O(h)     |
| 125  | Valid Palindrome                                                | Easy       | [EasyQuestions/125.py](EasyQuestions/125.py)       | Filter + normalize + two-way check via reverse | O(n)              | O(n)     |
| 1266 | Minimum Time Visiting All Points                                | Easy       | [EasyQuestions/1266.py](EasyQuestions/1266.py)     | Chebyshev distance accumulation                | O(n)              | O(1)     |
| 1365 | How Many Numbers Are Smaller Than the Current Number            | Easy       | [EasyQuestions/1365.py](EasyQuestions/1365.py)     | Sort + first-index hash map                    | O(n log n)        | O(n)     |
| 1672 | Richest Customer Wealth                                         | Easy       | [EasyQuestions/1672.py](EasyQuestions/1672.py)     | Row-wise sum and running maximum               | O(m\*n)           | O(1)     |
| 1684 | Count the Number of Consistent Strings                          | Easy       | [EasyQuestions/1684.py](EasyQuestions/1684.py)     | Allowed-character set with all-check           | O(n\*m)           | O(k)     |
| 169  | Majority Element                                                | Easy       | [EasyQuestions/169.py](EasyQuestions/169.py)       | Boyer-Moore voting algorithm                   | O(n)              | O(1)     |
| 1979 | Find Greatest Common Divisor of Array                           | Easy       | [EasyQuestions/1979.py](EasyQuestions/1979.py)     | Euclidean algorithm on min and max             | O(log n)          | O(1)     |
| 1929 | Concatenation of Array                                          | Easy       | [EasyQuestions/1929.py](EasyQuestions/1929.py)     | Concatenate array with itself                  | O(n)              | O(n)     |
| 2011 | Final Value of Variable After Performing Operations             | Easy       | [EasyQuestions/2011.py](EasyQuestions/2011.py)     | Linear simulation                              | O(n)              | O(1)     |
| 217  | Contains Duplicate                                              | Easy       | [EasyQuestions/217.py](EasyQuestions/217.py)       | Hash set length comparison                     | O(n)              | O(n)     |
| 2235 | Add Two Integers                                                | Easy       | [EasyQuestions/2235.py](EasyQuestions/2235.py)     | Direct arithmetic addition                     | O(1)              | O(1)     |
| 231  | Power of Two                                                    | Easy       | [EasyQuestions/231.py](EasyQuestions/231.py)       | Bitwise power-of-two check                     | O(1)              | O(1)     |
| 2413 | Smallest Even Multiple                                          | Easy       | [EasyQuestions/2413.py](EasyQuestions/2413.py)     | Parity check and conditional doubling          | O(1)              | O(1)     |
| 242  | Valid Anagram                                                   | Easy       | [EasyQuestions/242.py](EasyQuestions/242.py)       | Compare letter frequencies                     | O(n)              | O(1)     |
| 2469 | Convert the Temperature                                         | Easy       | [EasyQuestions/2469.py](EasyQuestions/2469.py)     | Direct Celsius conversion formulas             | O(1)              | O(1)     |
| 2496 | Convert the Temperature                                         | Easy       | [EasyQuestions/2496.py](EasyQuestions/2496.py)     | Direct Celsius conversion formulas             | O(1)              | O(1)     |
| 3894 | Traffic Signal                                                  | Easy       | [EasyQuestions/3894.py](EasyQuestions/3894.py)     | Conditional signal state lookup                | O(1)              | O(1)     |
| 268  | Missing Number                                                  | Easy       | [EasyQuestions/268.py](EasyQuestions/268.py)       | Arithmetic sum difference                      | O(n)              | O(1)     |
| 2769 | Find the Maximum Achievable Number                              | Easy       | [EasyQuestions/2769.py](EasyQuestions/2769.py)     | Direct arithmetic transformation               | O(1)              | O(1)     |
| 2798 | Number of Employees Who Met the Target                          | Easy       | [EasyQuestions/2798.py](EasyQuestions/2798.py)     | Count hours meeting or exceeding target        | O(n)              | O(1)     |
| 283  | Move Zeroes                                                     | Easy       | [EasyQuestions/283.py](EasyQuestions/283.py)       | Two-pointer in-place swapping                  | O(n)              | O(1)     |
| 2894 | Divisible and Non-divisible Sums Difference                     | Easy       | [EasyQuestions/2894.py](EasyQuestions/2894.py)     | Two filtered sums and subtraction              | O(n)              | O(1)     |
| 2942 | Find Words Containing Character                                 | Easy       | [EasyQuestions/2942.py](EasyQuestions/2942.py)     | Scan words and collect matching indices        | O(n\*m)           | O(k)     |
| 326  | Power of Three                                                  | Easy       | [EasyQuestions/326.py](EasyQuestions/326.py)       | Recursive divisibility by 3                    | O(log n)          | O(log n) |
| 3274 | Check if Two Chessboard Squares Have the Same Color             | Easy       | [EasyQuestions/3274.py](EasyQuestions/3274.py)     | Parity comparison of coordinate encodings      | O(1)              | O(1)     |
| 3498 | Reverse Degree of a String                                      | Easy       | [EasyQuestions/3498.py](EasyQuestions/3498.py)     | Reverse alphabet position weighted sum         | O(n)              | O(1)     |
| 3516 | Find Closest Person                                             | Easy       | [EasyQuestions/3516.py](EasyQuestions/3516.py)     | Compare absolute distances to target           | O(1)              | O(1)     |
| 3701 | Alternating Sum                                                 | Easy       | [EasyQuestions/3701.py](EasyQuestions/3701.py)     | Pairwise alternating addition and subtraction  | O(n)              | O(1)     |
| 3794 | Reverse Prefix                                                  | Easy       | [EasyQuestions/3794.py](EasyQuestions/3794.py)     | Reverse prefix with string slicing             | O(n)              | O(n)     |
| 3110 | Score of a String                                               | Easy       | [EasyQuestions/3110.py](EasyQuestions/3110.py)     | Adjacent ASCII difference accumulation         | O(n)              | O(1)     |
| 3190 | Find Minimum Operations to Make All Elements Divisible by Three | Easy       | [EasyQuestions/3190.py](EasyQuestions/3190.py)     | Count non-divisible elements                   | O(n)              | O(1)     |
| 448  | Find All Numbers Disappeared in an Array                        | Easy       | [EasyQuestions/448.py](EasyQuestions/448.py)       | Set membership scan                            | O(n)              | O(n)     |
| 771  | Jewels and Stones                                               | Easy       | [EasyQuestions/771.py](EasyQuestions/771.py)       | Count stones present in jewels string          | O(n\*m)           | O(1)     |
| 238  | Product of Array Except Self                                    | Medium     | [MediumQuestions/238.py](MediumQuestions/238.py)   | Two-pass prefix and postfix products           | O(n)              | O(1)     |
| 34   | Find First and Last Position of Element in Sorted Array         | Medium     | [MediumQuestions/34.py](MediumQuestions/34.py)     | Two binary searches                            | O(log n)          | O(1)     |
| 49   | Group Anagrams                                                  | Medium     | [MediumQuestions/49.py](MediumQuestions/49.py)     | Character frequency signature hashing          | O(n\*k)           | O(n\*k)  |
| 72   | Edit Distance                                                   | Medium     | [MediumQuestions/72.py](MediumQuestions/72.py)     | Top-down dynamic programming with memoization  | O(m\*n)           | O(m\*n)  |
| 75   | Sort Colors                                                     | Medium     | [MediumQuestions/75.py](MediumQuestions/75.py)     | Dutch national flag three-pointer partition    | O(n)              | O(1)     |
| 98   | Validate Binary Search Tree                                     | Medium     | [MediumQuestions/98.py](MediumQuestions/98.py)     | DFS bounds validation                          | O(n)              | O(h)     |
| 1143 | Longest Common Subsequence                                      | Medium     | [MediumQuestions/1143.py](MediumQuestions/1143.py) | Bottom-up dynamic programming table            | O(m\*n)           | O(m\*n)  |
| 153  | Find Minimum in Rotated Sorted Array                            | Medium     | [MediumQuestions/153.py](MediumQuestions/153.py)   | Binary search on pivot side                    | O(log n)          | O(1)     |
| 4    | Median of Two Sorted Arrays                                     | Hard       | [HardQuestions/4.py](HardQuestions/4.py)           | Partition-based binary search                  | O(log(min(m, n))) | O(1)     |
| 42   | Trapping Rain Water                                             | Hard       | [HardQuestions/42.py](HardQuestions/42.py)         | Two pointers with running boundaries           | O(n)              | O(1)     |

<!-- SOLVED_TABLE_END -->

## Run a Solution Locally

Most files contain a `Solution` class method matching LeetCode signatures.

1. Open the target file.
2. Add a small driver block for local testing if needed.
3. Run with Python:

```bash
python EasyQuestions/125.py
```

On some Windows setups, use:

```bash
py EasyQuestions/125.py
```

## Notes

- Some files use type hints like `List[int]` without importing `List` from `typing`. This is fine on LeetCode if their runner accepts it, but for strict local execution you may need:

```python
from typing import List
```

- Tree problems include a local `TreeNode` class for clarity and compatibility with LeetCode-style signatures.

## Goals

- Keep solutions readable and interview-ready.
- Prefer optimal or near-optimal approaches.
- Continue expanding medium and hard coverage.

## Contribution

If you want to suggest improvements:

1. Open an issue describing the optimization or bug.
2. Include input/output examples and expected complexity.
3. Keep changes focused and easy to review.

## License

This repository is for learning and interview preparation.
Add a license file if you plan to distribute it publicly.
