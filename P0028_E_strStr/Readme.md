## 28. Find the Index of the First Occurrence in a String

Example 1:\
Input: haystack = "sadbutsad", needle = "sad"\
Output: 0\
Explanation: "sad" occurs at index 0 and 6.\
The first occurrence is at index 0, so we return 0.

Example 2:\
Input: haystack = "leetcode", needle = "leeto"\
Output: -1\
Explanation: "leeto" did not occur in "leetcode", so we return -1.

### gpt建議:
- 使用slide window （注意索引值範圍）

```python
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle) 
        for right in range(n-1, len(haystack)):
            left = right - (n - 1)
            if  haystack[left:right + 1] == needle:
                return left
        return -1
```