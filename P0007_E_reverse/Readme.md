## 7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Example 1:\
Input: x = 123\
Output: 321

Example 2:\
Input: x = -123\
Output: -321

Example 3:\
Input: x = 120\
Output: 21

### Note:
- 除法商數餘數

```python
class Solution:
    def reverse(self, x: int) -> int:
        n =  abs(x) 
        rev = 0
        while n:
            rev = rev * 10 + n % 10
            n = n // 10
            if 2**31-1 < rev: 
                return 0

        rev = rev if x > 0 else -rev
        return rev
```