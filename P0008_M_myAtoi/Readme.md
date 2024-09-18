## 8. String to Integer (atoi)

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

- Whitespace: Ignore any leading whitespace (" ").
- Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
- Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
- Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.\
Return the integer as the final result.

Example 1:\
Input: s = "42"\
Output: 42\
Explanation:\
The underlined characters are what is read in and the caret is the current reader position.\
Step 1: "42" (no characters read because there is no leading whitespace)\
         ^\
Step 2: "42" (no characters read because there is neither a '-' nor '+')\
         ^\
Step 3: "42" ("42" is read in)\
           ^

Example 2:\
Input: s = " -042"\
Output: -42\
Explanation:\
Step 1: "   -042" (leading whitespace is read and ignored)\
            ^\
Step 2: "   -042" ('-' is read, so the result should be negative)\
             ^\
Step 3: "   -042" ("042" is read in, leading zeros ignored in the result)\
               ^

Example 3:\
Input: s = "1337c0d3"\
Output: 1337\
Explanation:\
Step 1: "1337c0d3" (no characters read because there is no leading whitespace)\
         ^\
Step 2: "1337c0d3" (no characters read because there is neither a '-' nor '+')\
         ^\
Step 3: "1337c0d3" ("1337" is read in; reading stops because the next character is a non-digit)\
             ^

Example 4:\
Input: s = "0-1"\
Output: 0\
Explanation:\
Step 1: "0-1" (no characters read because there is no leading whitespace)\
         ^\
Step 2: "0-1" (no characters read because there is neither a '-' nor '+')\
         ^\
Step 3: "0-1" ("0" is read in; reading stops because the next character is a non-digit)\
          ^\

Example 5:\
Input: s = "words and 987"\
Output: 0\
Explanation:\
Reading stops at the first non-digit character 'w'.\

### Note:
1. 移除空白
2. 如果全部都是空白，回傳0
3. 判斷符號
4. 計算數字
5. 判斷有沒有超出範圍

### gpt建議:
- 轉換結果時，不要全部一起轉換

```python
class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        # 忽略前面空白字符
        while i < n and s[i] == ' ':
            i += 1
        # 如果已經到達字符串末尾，返回 0
        if i == n:
            return 0
        
        # 處理符號
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        
        # 轉換數字
        result = 0
        # ref https://www.geeksforgeeks.org/python-extract-numbers-from-string/
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        # 應用符號
        result *= sign
        
        # 結果的範圍限制
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        
        return result
``` 