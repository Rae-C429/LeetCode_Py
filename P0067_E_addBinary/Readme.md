## 67. Add Binary

Given two binary strings a and b, return their sum as a binary string.

Example 1:\
Input: a = "11", b = "1"\
Output: "100"

Example 2:\
Input: a = "1010", b = "1011"\
Output: "10101"

### Note:
1. 從最小位數開始計算
2. 為是不夠補0
3. 利用2的商數餘數

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1  
        
        while i >= 0 or j >= 0 or carry:
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0
            total = bit_a + bit_b + carry
            carry = (total)//2
            result.append(str(total%2))
            i-=1
            j-=1

        return "".join(reversed(result))
```