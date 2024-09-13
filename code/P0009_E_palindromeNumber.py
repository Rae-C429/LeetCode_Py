class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 檢查數字是否小於0或結尾是0的數
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        #  反轉數字
        reverseX = 0
        temp = x
        while temp!= 0:
            reverseX = reverseX * 10 + temp % 10 
            temp //= 10
        if reverseX == x:
            return True 