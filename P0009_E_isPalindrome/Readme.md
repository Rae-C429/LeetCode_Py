## 9. Palindrome Number
Given an integer `x`, return true if `x` is a palindrome, and false otherwise.

Example 1:\
Input: x = 121\
Output: true

Example 2:\
Input: x = -121\
Output: false

### Note:
- 反轉數字

### gpt建議:
- 可以先排除`0`或是被`10`整除的數字

```python
def isPalindrome(self, x:int) -> bool:
    # 檢查數字是否小於0或結尾是0的數
    if x <= 0 or  (x % 10 == 0 and x !=0):
        return False
    # 反轉數字
    reverseX = 0
    temp = x
    while temp != 0:
        digit = temp % 10
        reverseX = reversX * 10 + digit
        temp //= 10  
    
    return reverseX == x
```