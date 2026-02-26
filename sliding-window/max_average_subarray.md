# Maximum Average Subarray I

**Pattern:** Sliding Window  

---

## 🧠 Problem Summary

Given an integer array `nums` and an integer `k`,  
find the contiguous subarray of length `k` that has the maximum average value.

---

## ❌ Brute Force Approach

- Calculate sum of every subarray of size `k`
- Compare each
- Time Complexity: O(n * k)

This recalculates overlapping values repeatedly.

---

## ✅ Optimized Approach (Sliding Window)

1. Compute sum of first `k` elements.
2. Slide the window:
   - Add new element
   - Subtract outgoing element
3. Track maximum window sum.

---

## ⏱ Time Complexity

O(n)

---

## 🧮 Space Complexity

O(1)

---

## 🔍 Why Sliding Window Works

Because the window size is fixed (`k`),  
we reuse previous computation efficiently instead of recalculating from scratch.
