class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        carry = 1
        while n >= 0 and carry == 1:
            digits[n] += carry
            carry = 0
            if digits[n] == 10:
                digits[n] = 0
                n -= 1
                carry = 1
        # 處理最大位數進位
        if digits[0] == 0:
            # ref https://www.geeksforgeeks.org/python-perform-append-at-beginning-of-list/
            digits.insert(0, 1)
        return digits
