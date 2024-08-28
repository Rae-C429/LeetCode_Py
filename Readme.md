# LeetCode Python
## 1.Two Sum
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
    # 當數字長度為奇數時，reverseHalf // 10 去掉中間數字
    return reverseHalf == temp or reverseHalf == temp // 10
```

## 13.Roman to Integer
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Example 1:
Input: s = "III" =>1+1+1
Output: 3

Example 2:
Input: s = "LVIII"=>3+5+10
Output: 58
題目要求將提供的羅馬數字(`string`)成阿拉伯數字(`int`)，在羅馬字中出小數出線在前面時代表要用減的 ex:IV = 5-1 =4

### 解題想法
1. 要先做出一個羅馬數字`dict`
2. 字串是字元序列組成的，利用索引直來比大小
3. 注意！字串後一個字元是沒有東西好比的

### 解答
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
            if romanNum[s[i]] < romanNum[s[i+1]] and i < len(s):
                intNum = intNum - romanNum[s[i]]

            # 一般情況
            else:
                intNum = intNum + romanNum[s[i]]

            return intNum
```

## 2.Add Two Numbers(Med.)
給您兩個表示兩個非負整數的非空鍊錶。這些數字以相反的順序存儲，並且每個節點都包含一個數字。將兩個數字相加並以鍊錶形式傳回總和。

Example 1
![alt text](image.png)

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

### 解答
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Optional 是 typing 模塊中的一个泛型類型，表示某個變量要麽是指定的類型（這裡是 ListNode），要麽是 None。
        # 創建一個虛擬的節點頭
        dummyHead = ListNode(0)
        # 創建指針只先目前位置
        current = dummyHead
        # 初始化進位
        carry = 0
        # 計算l1,l2的值
        while l1 is not None or l2 is not None:
            x = l1.val if is not None else 0
            y = l2.val if is not None else 0
            sum = x + y + carry
            # 進位計算
            carry = carry // 10
            # 將計算出的答案增加至下一個節點
            current.next = ListNode(sum % 10)
            current = current.next
            # 前往l1,l2下一節點
            if l1 is not None:
                l1 = l1.next 
            if l2 is not None:
                l2 = l2.next

            if carry > 0:
                current.next = ListCode(carry)
                
            return dummyHead.next

```

## 14.Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

### 解題想法
1. 取第一個值作為比較對象
2. 注意字串長度
3. 先整理在比較

### 解答
```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None:
            return ""
        strs = sorted(strs)
        prefix = ""
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return prefix 
            prefix += first[i]
        return prefix
```
`sorted()` 會先按照字母順序，如果字母相同長度較短的會在前面

### 20.Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

### 解題想法
1. 括號都是成對的，利用`dict` key:value
2. 利用stack先進後出，將左括號存入

### 解答
```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        par = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char not in par:
                stack.append(char)
            else:
                top = stack.pop() if stack else False
                if top != par[char]:
                    return False
                
        return not stack 
```
`if char not in par:` 用來檢查key，若想檢查value請用`par.value()`
 
 ### 3.Longest Substring Without Repeating Characters(med)

Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### 解題想法
題目的是要找出字串中最長且不重複的子字串。
認識slide window
```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 創建空集合用來裝子字串
        sub = set()
        # 左邊窗戶
        left = 0
        maxLen = 0
        # 開始檢查
        for right in range(len(s)):
            if s[right] not in sub:
                sub.add(s[right])
                # 計算子字串長度
                maxLen = max(maxLen, right - left + 1)
            # 如果遇到重複刪除前面所有字元
            while s[right] in sub:
                sub.remove(left)
                left += 1
            sub.add(s[right])
        return maxLen
```
其實可以寫得更漂亮:酷
```python
for right in range(len(s)):            
            sub.add(s[right])
            maxLen = max(maxLen, right - left + 1)
            # 如果遇到重複刪除前面所有字元
            while s[right] in sub:
                sub.remove(left)
                left += 1            
```
