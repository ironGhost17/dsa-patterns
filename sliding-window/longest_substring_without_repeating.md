# Longest Substring Without Repeating Characters

**Pattern:** Sliding Window (Variable Size)

---

## 🧠 Problem Summary

Given a string `s`, find the length of the longest substring without repeating characters.

---

## ❌ Brute Force Approach

- Generate all substrings
- Check if each substring has unique characters
- Time Complexity: O(n³) in worst case

Clearly inefficient.

---

## ✅ Optimized Approach (Sliding Window)

1. Use two pointers (`left` and `right`).
2. Maintain a set to track unique characters in the current window.
3. Expand `right`.
4. If duplicate found:
   - Shrink window from `left` until duplicate is removed.
5. Track maximum window length.

---

## ⏱ Time Complexity

O(n)

Each character is added and removed at most once.

---

## 🧮 Space Complexity

O(min(n, charset))



---

## 🔍 Why Sliding Window Works

We dynamically adjust the window size to maintain the constraint (no duplicates),
instead of recomputing substrings repeatedly.


---

**Source:** LeetCode  
**Problem Link:** https://leetcode.com/problems/longest-substring-without-repeating-characters/
