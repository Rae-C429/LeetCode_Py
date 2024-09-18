class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # slide window 注意索引值範圍
        n = len(needle) 
        for right in range(n-1, len(haystack)):
            left = right - (n - 1)
            if  haystack[left:right + 1] == needle:
                return left
        return -1

