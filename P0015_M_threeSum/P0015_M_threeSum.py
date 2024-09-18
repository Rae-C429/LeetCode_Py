class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        tri = []
        nums = sorted(nums)

        for i in range(len(nums)-2):
            # 檢查跟前一個有沒有相同
            # 不要跟下一個比不然會有漏網之魚
            if i > 0 and nums[i] == nums[i-1]:
                # print(i,"\n")
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left+=1
                elif total > 0:
                    right-=1
                else:
                    tri.append([nums[i], nums[left], nums[right]])
                    # 檢查框框內有沒有重複的，有的話要一直往內縮
                    while left < right and nums[left]==nums[left+1]:
                        left+=1
                    while left < right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
        return tri