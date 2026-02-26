# Two Sum II – Input Array Is Sorted

**Pattern:** Two Pointers  
**Problem Link:** https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

---

## 🧠 Problem Summary

Given a sorted array of integers `numbers`
and a target value, return the 1-based indices
of the two numbers such that they add up to target.

---

## ❌ Brute Force Approach

- Try all pairs
- Time Complexity: O(n²)

---

## ✅ Optimized Approach (Two Pointers)

1. Place one pointer at the start.
2. Place one pointer at the end.
3. Compute their sum.
4. If sum is too small → move left pointer.
5. If sum is too large → move right pointer.
6. Stop when target is found.

---

## ⏱ Time Complexity

O(n)

---

## 🧮 Space Complexity

O(1)

---

## 🔍 Why Two Pointers Works

Because the array is sorted, we can eliminate
half the possibilities at each step by adjusting pointers intelligently.
