class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 創建空集合用來裝子字串
        sub = set()
        # 左邊窗戶
        left = 0
        maxLen = 0
        # 開始檢查
        for right in range(len(s)):
            if s[right] not in sub:
                sub.add(s[right])
                # 計算子字串長度
                maxLen = max(maxLen, right - left + 1)
            # 如果遇到重複刪除前面所有字元
            while s[right] in sub:
                sub.remove(left)
                left += 1
            sub.add(s[right])
        return maxLen