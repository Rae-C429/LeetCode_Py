## 136. Single Number

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]\
Output: 1

Example 2:\
Input: nums = [4,1,2,1,2]\
Output: 4

Example 3:\
Input: nums = [1]\
Output: 1

### Note:
- 使用dict

```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        # 預設值為1如果重複+1
        for i in nums:
            if i in seen:
                seen[i] +=1  
            else:
                seen[i] = 1
        for key, val in seen.items():
            if val == 1: 
                return key
```