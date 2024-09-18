## 13. Roman to Integer
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

|Symbol|   Value|
|------|--------|
|I     |       1|
|V     |       5|
|X     |      10|
|L     |      50|
|C     |     100|
|D     |     500|
|M     |    1000|

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

- I can be placed before V (5) and X (10) to make 4 and 9. 
- X can be placed before L (50) and C (100) to make 40 and 90. 
- C can be placed before D (500) and M (1000) to make 400 and 900.

Example 1:\
Input: s = "III" =>1+1+1\
Output: 3

Example 2:\
Input: s = "LVIII"=>3+5+10\
Output: 58\

### Note:
1. 先做出一個羅馬數字`dict`
2. 字串是字元序列組成的，從左變最大位數開始計算
3. 利用索引直來比前後大小
3. 注意！字串後一個字元是沒有東西好比的

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        # 創建羅馬數字dict
        romanNum = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        intNum = 0
        # 檢查羅馬數字大小
        for i in range(len(s)):
            # 如果前面數字小於後面數字
            if i < len(s) and romanNum[s[i]] < romanNum[s[i+1]] :
                intNum = intNum - romanNum[s[i]]

            # 一般情況
            else:
                intNum = intNum + romanNum[s[i]]

            return intNum
```