class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0
        subSt = set()
        maxLen = 0

        for right in range(len(s)):
                # 如果不在subSt裡
                if s[right] not in subSt:
                    subSt.add(s[right])
                    maxLen = max(maxLen,right - left + 1)
                else:
                    while s[right] in subSt:
                        subSt.remove(s[left])
                        left+=1
                    subSt.add(s[right])
        return maxLen