class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        # 忽略前面空白字符
        while i < n and s[i] == ' ':
            i += 1
        # 如果已經到達字符串末尾，返回 0
        if i == n:
            return 0
        
        # 處理符號
        sign = 1
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        
        # 轉換數字
        result = 0
        # ref https://www.geeksforgeeks.org/python-extract-numbers-from-string/
        while i < n and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        # 應用符號
        result *= sign
        
        # 結果的範圍限制
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        
        return result


        