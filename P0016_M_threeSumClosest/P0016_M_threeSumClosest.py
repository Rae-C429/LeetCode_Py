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