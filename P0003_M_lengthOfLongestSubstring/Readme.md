## 3. Longest Substring Without Repeating Characters(med)

Given a string s, find the length of the longest substring without repeating characters.

Example 1:\
Input: s = "abcabcbb"\
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:\
Input: s = "bbbbb"\
Output: 1\
Explanation: The answer is "b", with the length of 1.

Example 3:\
Input: s = "pwwkew"\
Output: 3\
Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### gpt建議:
- 使用slide window

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 創建空集合用來裝子字串
        sub = set()
        # 左邊窗戶
        left = 0
        maxLen = 0
        # 開始檢查
        for right in range(len(s)):
            if s[right] not in sub:
                sub.add(s[right])
                # 計算子字串長度
                maxLen = max(maxLen, right - left + 1)
            # 如果遇到重複刪除前面所有字元
            while s[right] in sub:
                sub.remove(left)
                left += 1
            sub.add(s[right])
        return maxLen
```
其實可以寫得更漂亮:酷
```python
for right in range(len(s)):            
            sub.add(s[right])
            maxLen = max(maxLen, right - left + 1)
            # 如果遇到重複刪除前面所有字元
            while s[right] in sub:
                sub.remove(left)
                left += 1            
```