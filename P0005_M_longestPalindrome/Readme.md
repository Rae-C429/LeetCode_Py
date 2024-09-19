## 5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

Example 1:\
Input: s = "babad"\
Output: "bab"\
Explanation: "aba" is also a valid answer.

Example 2:\
Input: s = "cbbd"\
Output: "bb"

## gpt建議:
1. 寫一個比較左右字元的方程式
2. 比較奇數對稱和偶數對稱
 
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        def expandAroundCenter(left: int, right: int) -> str:
            # 擴展回文的核心邏輯
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # 當擴展結束時，返回回文子串
            return s[left + 1:right]
        
        longest_palindrome = ""
        
        for i in range(len(s)):
            # 奇數長度的回文
            odd_palindrome = expandAroundCenter(i, i)
            # 偶數長度的回文
            even_palindrome = expandAroundCenter(i, i + 1)
            
            # 更新最長回文子串
            if len(odd_palindrome) > len(longest_palindrome):
                longest_palindrome = odd_palindrome
            if len(even_palindrome) > len(longest_palindrome):
                longest_palindrome = even_palindrome
        
        return longest_palindrome
```