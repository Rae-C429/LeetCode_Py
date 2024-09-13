def TwoSum(self, nums:List[int], target:int) -> List[int]:
        # 創建字典
        num_map = {}
        # 檢查nums list裡的元素有沒有相加等於target的
        for i, num in enumerate(nums):
            complement = target - num # 計算當前補數
            if complement in num_map:# 檢查補數是否在num_map字典裡
            # 如果補數存在字典裡，回傳補數對應的索引和當前數字索引
                return [num_map[complement], i]
            # 如果不存在，儲存當前數字和索引於字典裡
            num_map[num] = i
        # 如果都沒有，回傳空的list
        return []