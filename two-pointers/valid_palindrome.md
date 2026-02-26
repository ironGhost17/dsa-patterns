# Valid Palindrome

**Pattern:** Two Pointers  
**Problem Link:** https://leetcode.com/problems/valid-palindrome/

---

## 🧠 Problem Summary

Given a string `s`, determine if it is a palindrome,
considering only alphanumeric characters and ignoring case.

---

## ❌ Brute Force Approach

- Filter string
- Reverse string
- Compare with original

Time Complexity: O(n)  
Space Complexity: O(n)

---

## ✅ Optimized Approach (Two Pointers)

1. Use two pointers:
   - One at the beginning
   - One at the end
2. Move inward
3. Skip non-alphanumeric characters
4. Compare lowercase characters

---

## ⏱ Time Complexity

O(n)

---

## 🧮 Space Complexity

O(1)

---

## 🔍 Why Two Pointers Works

We compare symmetric elements directly without creating a new string.
This avoids extra space and keeps the solution efficient.
