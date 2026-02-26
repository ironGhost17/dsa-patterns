# Sliding Window Pattern

## 📌 When to Use

Use this pattern when:
- The problem involves subarrays or substrings
- You need to calculate something over a contiguous range
- Brute force would be O(n²)
- Constraints suggest an O(n) solution

---

## 🧠 Core Idea

Maintain a running window using:
- Two pointers (left & right)
- A running sum or frequency map
- Expand and shrink dynamically

---

## 📚 Problems

1. Maximum Average Subarray I  
   - Fixed-size window  
   - Time: O(n)  
   - Space: O(1)

2. Longest Substring Without Repeating Characters  
   - Variable-size window  
   - Time: O(n)  
   - Space: O(n)
