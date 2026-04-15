# LeetCode Python Solutions

<!-- BADGES_START -->

![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)
![Solved](https://img.shields.io/badge/Solved-24-2ea44f)
![Easy](https://img.shields.io/badge/Easy-19-6ab04c)
![Medium](https://img.shields.io/badge/Medium-3-f39c12)
![Hard](https://img.shields.io/badge/Hard-2-e74c3c)
![Last Updated](https://img.shields.io/badge/Last%20Updated-2026--04--15-0366d6)

<!-- BADGES_END -->

A curated collection of my LeetCode solutions in Python, organized by difficulty.

## Overview

This repository contains concise and interview-focused implementations for LeetCode problems.

- Language: Python
- Total solved: 24
- Difficulty split:
  - Easy: 19
  - Medium: 3
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
|   |-- 2011.py
|   |-- 217.py
|   |-- 231.py
|   |-- 268.py
|   |-- 283.py
|   `-- 448.py
|-- MediumQuestions/
|   |-- 34.py
|   |-- 98.py
|   `-- 153.py
`-- HardQuestions/
    |-- 4.py
    `-- 42.py
```

## Solved Problems

<!-- SOLVED_TABLE_START -->

| #    | Problem                                                 | Difficulty | File                                             | Approach                                       | Time              | Space |
| ---- | ------------------------------------------------------- | ---------- | ------------------------------------------------ | ---------------------------------------------- | ----------------- | ----- |
| 1    | Two Sum                                                 | Easy       | [EasyQuestions/1.py](EasyQuestions/1.py)         | One-pass hash map                              | O(n)              | O(n)  |
| 13   | Roman to Integer                                        | Easy       | [EasyQuestions/13.py](EasyQuestions/13.py)       | Left-to-right numeral comparison               | O(n)              | O(1)  |
| 26   | Remove Duplicates from Sorted Array                     | Easy       | [EasyQuestions/26.py](EasyQuestions/26.py)       | Two-pointer overwrite                          | O(n)              | O(1)  |
| 27   | Remove Element                                          | Easy       | [EasyQuestions/27.py](EasyQuestions/27.py)       | Write-pointer compaction                       | O(n)              | O(1)  |
| 28   | Find the Index of the First Occurrence in a String      | Easy       | [EasyQuestions/28.py](EasyQuestions/28.py)       | Built-in substring search                      | O(n\*m)           | O(1)  |
| 66   | Plus One                                                | Easy       | [EasyQuestions/66.py](EasyQuestions/66.py)       | Right-to-left carry handling                   | O(n)              | O(1)  |
| 58   | Length of Last Word                                     | Easy       | [EasyQuestions/58.py](EasyQuestions/58.py)       | Strip and split string                         | O(n)              | O(n)  |
| 9    | Palindrome Number                                       | Easy       | [EasyQuestions/9.py](EasyQuestions/9.py)         | Reverse integer and compare                    | O(log n)          | O(1)  |
| 104  | Maximum Depth of Binary Tree                            | Easy       | [EasyQuestions/104.py](EasyQuestions/104.py)     | DFS recursion                                  | O(n)              | O(h)  |
| 111  | Minimum Depth of Binary Tree                            | Easy       | [EasyQuestions/111.py](EasyQuestions/111.py)     | DFS recursion with null-child handling         | O(n)              | O(h)  |
| 125  | Valid Palindrome                                        | Easy       | [EasyQuestions/125.py](EasyQuestions/125.py)     | Filter + normalize + two-way check via reverse | O(n)              | O(n)  |
| 1266 | Minimum Time Visiting All Points                        | Easy       | [EasyQuestions/1266.py](EasyQuestions/1266.py)   | Chebyshev distance accumulation                | O(n)              | O(1)  |
| 1365 | How Many Numbers Are Smaller Than the Current Number    | Easy       | [EasyQuestions/1365.py](EasyQuestions/1365.py)   | Sort + first-index hash map                    | O(n log n)        | O(n)  |
| 2011 | Final Value of Variable After Performing Operations     | Easy       | [EasyQuestions/2011.py](EasyQuestions/2011.py)   | Linear simulation                              | O(n)              | O(1)  |
| 217  | Contains Duplicate                                      | Easy       | [EasyQuestions/217.py](EasyQuestions/217.py)     | Hash set length comparison                     | O(n)              | O(n)  |
| 231  | Power of Two                                            | Easy       | [EasyQuestions/231.py](EasyQuestions/231.py)     | Bitwise power-of-two check                     | O(1)              | O(1)  |
| 268  | Missing Number                                          | Easy       | [EasyQuestions/268.py](EasyQuestions/268.py)     | Arithmetic sum difference                      | O(n)              | O(1)  |
| 283  | Move Zeroes                                             | Easy       | [EasyQuestions/283.py](EasyQuestions/283.py)     | Two-pointer in-place swapping                  | O(n)              | O(1)  |
| 448  | Find All Numbers Disappeared in an Array                | Easy       | [EasyQuestions/448.py](EasyQuestions/448.py)     | Set membership scan                            | O(n)              | O(n)  |
| 34   | Find First and Last Position of Element in Sorted Array | Medium     | [MediumQuestions/34.py](MediumQuestions/34.py)   | Two binary searches                            | O(log n)          | O(1)  |
| 98   | Validate Binary Search Tree                             | Medium     | [MediumQuestions/98.py](MediumQuestions/98.py)   | DFS bounds validation                          | O(n)              | O(h)  |
| 153  | Find Minimum in Rotated Sorted Array                    | Medium     | [MediumQuestions/153.py](MediumQuestions/153.py) | Binary search on pivot side                    | O(log n)          | O(1)  |
| 4    | Median of Two Sorted Arrays                             | Hard       | [HardQuestions/4.py](HardQuestions/4.py)         | Partition-based binary search                  | O(log(min(m, n))) | O(1)  |
| 42   | Trapping Rain Water                                     | Hard       | [HardQuestions/42.py](HardQuestions/42.py)       | Two pointers with running boundaries           | O(n)              | O(1)  |

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
