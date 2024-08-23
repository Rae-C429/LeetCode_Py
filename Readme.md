# LeetCode Python
## 2.Two Sum
題目提供：
```python
class Solution(object):
    def TwoSum(self, nums:List[int], target:int) -> List[int]:
```
題目給了一個 `class`，而`class`類中的函數必須包含`self`參數。通過 `self`，你可以在方法內部訪問實例變量和其他方法。它允許你在類的不同方法之間共享數據和狀態。

`nums: List[int]`: 輸入參數，nums 是一個整數列表。List[int] 是 Python 的類型註釋，表示 nums 是一個包含整數的列表。
`target: int`: 另一個輸入參數，target 是一個整數，表示我們要查找的兩個數字的和。

`-> List[int]`: 函數的返回類型註釋。`->` 表示函數的返回類型。`List[int]` 表示這個函數會返回一個由整數組成的列表。這有助於了解函數的輸出是什麼類型，並且能夠進行靜態類型檢查。
### 解答
```python
    def TwoSum(self, nums:List[int], target:int) -> List[int]:
        # 創建字典
        num_map = {}
        # 檢查nums list裡的元素有沒有相加等於target的
        for i, num in enurmerate(nums):
            complement = target - num # 計算當前補數
            if complement in num_map:# 檢查補數市府在num_map字典裡
            # 如果補數存在字典裡，回傳補數對應的索引和當前數字索引
                return [num_map[complement], i]
            # 如果不存在，儲存當前數字和索引於字典裡
            num_map[num] = i
        # 如果都沒有，回傳空的list
        return []
```

` for i, num in enurmerate(nums): `這段語法中，每次迭代時，enumerate(nums) 返回的一對（索引和值）會被自動解包成兩個變量：i 和 num。
ex:`[(0, nums[0]), (1, nums[1]).....]`

## 9.Palindrome Number
Given an integer `x`, return true if `x` is a palindrome, and false otherwise.

Example 1:
Input: x = 121
Output: true

Input: x = -121
Output: false

### 方法一：反轉全部數字
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

### 方法二：反轉一半數字
```python
def isPalindrome(self, x:int) -> bool:
    # 檢查數字是否小於0或結尾是0的數
    if x <= 0 or  (x % 10 == 0 and x !=0):
        return False
    # 反轉數字
    reverseHalf = 0
    temp = x
    while temp > reverseHalf:
        digit = temp % 10
        reverseHalf = reverseHalf * 10 + digit
        temp //= 10  
    # 當數字長度為奇數時，reversedHalf // 10 去掉中間數字
    return reverseHalf == temp or reverseHalf == temp // 10
```
