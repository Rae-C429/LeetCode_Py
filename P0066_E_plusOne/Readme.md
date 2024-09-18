## 66. Plus One

Example 1:\
Input: digits = [1,2,3]\
Output: [1,2,4]\
Explanation: The array represents the integer 123.\
Incrementing by one gives 123 + 1 = 124.\
Thus, the result should be [1,2,4].

Example 2:\
Input: digits = [4,3,2,1]\
Output: [4,3,2,2]\
Explanation: The array represents the integer 4321.\
Incrementing by one gives 4321 + 1 = 4322.\
Thus, the result should be [4,3,2,2].

Example 3:\
Input: digits = [9]\
Output: [1,0]\
Explanation: The array represents the integer 9.\
Incrementing by one gives 9 + 1 = 10.\
Thus, the result should be [1,0].

### Note:
1. 先處理最小位數（列表中最後一個元素）
2. 處理最大位數進位（列表中第一個元素）

```python
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        carry = 1
        while n >= 0 and carry == 1:
            digits[n] += carry
            carry = 0
            if digits[n] == 10:
                digits[n] = 0
                n -= 1
                carry = 1
        # 處理最大位數進位
        if digits[0] == 0:
            # ref https://www.geeksforgeeks.org/python-perform-append-at-beginning-of-list/
            digits.insert(0, 1)
        return digits
```