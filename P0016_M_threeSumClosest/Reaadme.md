## 16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.\
Return the sum of the three integers.\
You may assume that each input would have exactly one solution.

Example 1:\
Input: nums = [-1,2,1,-4], target = 1\
Output: 2\
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:\
Input: nums = [0,0,0], target = 1\
Output: 0\
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

### Note:
1. 將提供的列表先進行排序
2. 固定一個值，滑動其他兩個值（slide window），尋找最接近的值

### gpt建議：
- 不需要特別跳過重複的數字，因問目的是尋找最接近值

```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 先對數組排序
        nums = sorted(nums)
        n = len(nums)
        # 初始化 sum3 為前三個數字的和
        sum3 = sum(nums[:3])
        currentSum = 0

        # 開始遍歷數組
        for i in range(n):
            left = i+1
            right = n-1
            
            # 使用雙指針進行搜索
            while left < right:
                currentSum  = nums[i] + nums[left] + nums[right]

                # 使用雙指針進行搜索
                if abs(currentSum - target) < abs(sum3 - target):
                    sum3 = currentSum
    
                # 調整雙指針
                if currentSum < target:
                    left+=1
                elif currentSum > target:
                    right-=1
                    
                # 如果等於目標值，直接返回
                else :
                    return target
        return sum3
```