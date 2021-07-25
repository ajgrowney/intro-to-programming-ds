# Heap
## Description
Optimized for tracking largest (MaxHeap) / smallest (MinHeap) values. A complete binary tree that is either empty or whose root contains a value larger (MaxHeap) / smaller (MinHeap) than all of its children. Each of its children is also a heap.
Used to implement the more complex data structure known as the priority queue.

## Functions
1) peek_top() -> int
    - Time Complexit: O(1)
2) add(new_item) -> bool
    - Time Complexit: O(log(k))
3) remove() -> bool
    - Time Complexity: O(log(k))
4) heapify(arr) -> heap
    - Time Complexit: O(n*log(k))

## Executive Class
The goal of this file is to show how you can heapify a list in O(n*log(k)) time and add elements to it in O(log(k)) time