class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # 移除最後面空格
        # ref https://www.geeksforgeeks.org/python-string-rstrip/
        s = s.rstrip()
        n = len(s) - 1
        lastLen = 0
        while n >= 0 and s[n] != ' ':
            n -=1
            lastLen += 1
        return lastLen

        