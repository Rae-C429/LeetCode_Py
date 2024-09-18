class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 雙指針
        k = 0
        for i in nums:
            if i!=val:
                nums[k] = i
                k+=1
        return k