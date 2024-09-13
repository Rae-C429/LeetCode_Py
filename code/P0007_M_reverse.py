class Solution:
    def reverse(self, x: int) -> int:
        n =  abs(x) if x < 0 else x
        rev = 0
        while n:
            rev = rev * 10 + n % 10
            n = n // 10
            if 2**31-1 < rev: 
                return 0

        rev = rev if x > 0 else -rev
        return rev