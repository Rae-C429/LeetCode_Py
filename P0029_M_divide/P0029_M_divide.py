class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        # 確定結果的符號
        neg = dividend < 0 != divisor < 0
        # 使用絕對值進行計算
        dividend = abs(dividend)
        divisor = abs(divisor)
        quotient = 0
        while dividend >= divisor:
            multiple = 1
            currentdivisor = divisor
            while dividend >= (currentdivisor << 1):
                # 一次增加2倍
                currentdivisor <<= 1
                # 計算倍數
                multiple <<= 1
            dividend -= currentdivisor
            quotient += multiple
        if neg:
            quotient = -quotient
        if quotient > 2**31-1:
            return 2**31-1
        if quotient < -2**31:
            return -2**31
        return  quotient 