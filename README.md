# Data Structures and Algorithms Toolkit

A beginner-friendly Python command-line project demonstrating classic searching and sorting algorithms and common data structures. Implementations are written for learning and testing, not as replacements for Python's optimized built-in tools.

## Features
- Linear search and binary search
- Bubble, selection, insertion, and merge sort
- Stack operations (LIFO) and queue operations (FIFO)
- Singly linked list: append, prepend, find, delete
- Binary search tree: insert, search, inorder/preorder/postorder traversals
- Input validation in the CLI
- Automated tests with Python's built-in `unittest`
- No third-party dependencies

## Requirements
Python 3.10 or newer recommended. Works on Windows, macOS, and Linux.

## Run
From the project root:
```bash
py main.py
```
If `py` is unavailable, use `python main.py` or `python3 main.py`.

## Test
```bash
py -m unittest discover -s tests -v
```

## Project structure
```text
data-structures-algorithms-toolkit/
├── main.py
├── dsa_toolkit/
│   ├── searching.py
│   ├── sorting.py
│   ├── stack.py
│   ├── queue.py
│   ├── linked_list.py
│   └── binary_search_tree.py
├── tests/
└── screenshots/
```

## Complexity overview
| Algorithm / operation | Typical time | Notes |
|---|---:|---|
| Linear search | O(n) | Works on unsorted lists |
| Binary search | O(log n) | Requires ascending-sorted input |
| Bubble sort | O(n²) worst | Early exit on already sorted input |
| Selection sort | O(n²) | Repeatedly selects smallest remaining value |
| Insertion sort | O(n²) worst | O(n) best case for sorted input |
| Merge sort | O(n log n) | O(n) extra space |
| Stack push/pop | O(1) | List-backed |
| Queue enqueue/dequeue | O(1) | Uses `collections.deque` |
| Linked list search/delete | O(n) | Traverses nodes |
| BST search/insert | O(log n) average, O(n) worst | Not self-balancing |

## Learning outcomes
Practice iteration, recursion, algorithm analysis, LIFO/FIFO behavior, linked nodes, tree traversal, and unit testing.

## Limitations and extensions
This is a command-line learning project. The binary search tree is not self-balancing. Possible extensions include a Tkinter visualizer, heaps, hash tables, graph traversal, and benchmark comparisons.

Commit work as you actually implement and test it; do not backdate Git history or claim a historical college submission that did not occur.
