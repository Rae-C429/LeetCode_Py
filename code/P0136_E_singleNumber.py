class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xorlist = {}
        for i in nums:
            if i in xorlist:
                xorlist[i] +=1  
            else:
                xorlist[i] = 1
        for key, val in xorlist.items():
            if val == 1: 
                return key