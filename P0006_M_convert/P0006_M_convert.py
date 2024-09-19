class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows>len(s):
            return s
        # 創建一個大小為 numRows 的列表
        z1 = [""]*numRows
        # 方向
        j = 1
        #當前的行號
        current_row = 0
        for i in s:
            z1[current_row]+=i
            if current_row == numRows-1:
                j = -1 
            elif current_row == 0:
                j = 1 
            current_row += j
        return ''.join(z1)