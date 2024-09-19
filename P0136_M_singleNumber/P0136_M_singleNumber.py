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