class Solution:
    def romanToInt(self, s: str) -> int:
        # 創建羅馬數字dict
        romanMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        numInt = 0
        # 檢查羅馬數字大小
        for i in range(len(s)):
            # 如果前面數字小於後面數字
            if i < len(s)-1 and romanMap[s[i]] < romanMap[s[i+1]]:
                numInt = numInt - romanMap[s[i]]
            # 一般情況
            else:
                numInt = numInt + romanMap[s[i]]

        return numInt