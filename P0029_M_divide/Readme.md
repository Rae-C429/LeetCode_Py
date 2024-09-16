## 29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.\

Return the quotient after dividing dividend by divisor.

Note: integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 

Example 1:\
Input: dividend = 10, divisor = 3\
Output: 3\
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:\
Input: dividend = 7, divisor = -3\
Output: -2\
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

### Note:
1. 題目禁止使用 `/`、`%`、`*`
2. 利用減號
3. 將除數與被除數、都轉為正號
### gpt建議:
1. 使用位運算（bitwise shift），減少運算時間，每次將除數左移一位，相當於除數乘以2
2. 使用雙層迴圈更高效

```python
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        # 確定結果的符號
        neg = (dividend < 0) != (divisor < 0)
        # 使用絕對值進行計算
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            multiple = 1
            currentdivisor = divisor
            while dividend >= (currentdivisor << 1):
                # 一次增加2倍
                currentdivisor <<= 1
                # 計算倍數
                multiple <<= 1
            dividend -= currentdivisor
            print('dividend',dividend)
            quotient += multiple
        print(2**31-1)
        if neg:
            quotient = -quotient
        if quotient > 2**31-1:
            return 2**31-1
        if quotient < -2**31:
            return -2**31
        return  quotient 
```
