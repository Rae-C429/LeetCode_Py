## 12. Integer to Roman

Seven different symbols represent Roman numerals with the following values:

|Symbol|   Value|
|------|--------|
|I     |       1|
|V     |       5|
|X     |      10|
|L     |      50|
|C     |     100|
|D     |     500|
|M     |    1000|\

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:
4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).

Example 1:\
Input: num = 3749\
Output: "MMMDCCXLIX"
Explanation:\
3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)\
 700 = DCC as 500 (D) + 100 (C) + 100 (C)\
  40 = XL as 10 (X) less of 50 (L)\
   9 = IX as 1 (I) less of 10 (X)\
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

Example 2:\
Input: num = 58\
Output: "LVIII"

Example 3\
Input: num = 1994\
Output: "MCMXCIV"

### gpt建議:
1. 使用 dict
2. 從高位數開始計算

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        roman={
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        ans = ''
        for n in [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]:
            while num >= n:
                num -= n
                ans += roman[n]
        return ans
```