class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        # 設定邊界一定要設在有效索引內
        while left <= right: #設定條件要注意
            mid = left+(right-left)//2
            if target < nums[mid]:
                right = mid-1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return left