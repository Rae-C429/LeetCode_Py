## 14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.If there is no common prefix, return an empty string "".

Example 1:\
Input: strs = ["flower","flow","flight"]\
Output: "fl"

Example 2:\
Input: strs = ["dog","racecar","car"]\
Output: ""\
Explanation: There is no common prefix among the input strings.

### gpt建議:
1. 先將strs排序
2. 比較第一個與最後一個字串即可

`sorted()` 會先按照字母順序，如果字母相同長度較短的會在前面

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None:
            return ""
        # 字串排序
        strs = sorted(strs)

        # 創建空自創儲存相通字串
        prefix = ""

        # 比較第一個與最後一個字串
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return prefix 
            prefix += first[i]
        return prefix
```
