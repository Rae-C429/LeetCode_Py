## 58. Length of Last Word

Example 1:\
Input: s = "Hello World"\
Output: 5\
Explanation: The last word is "World" with length 5.

Example 2:\
Input: s = "   fly me   to   the moon  "\
Output: 4\
Explanation: The last word is "moon" with length 4.

Example 3:\
Input: s = "luffy is still joyboy"\
Output: 6\
Explanation: The last word is "joyboy" with length 6.

### Note:
1. 移除最後空格
2. 從最後面開始計算遇到空白前的文字長度

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 移除最後面空格
        # ref https://www.geeksforgeeks.org/python-string-rstrip/
        s = s.rstrip()
        n = len(s) - 1
        lastLen = 0
        while n >= 0 and s[n] != ' ':
            n -=1
            lastLen += 1
        return lastLen
```