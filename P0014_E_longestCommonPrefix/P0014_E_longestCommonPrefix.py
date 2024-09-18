class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None:
            return ""
        # 字串排序
        strs = sorted(strs)

        # 創建空自創儲存相通字串
        prefix = ""

        # 比較第一個與最後一個字串
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return prefix 
            prefix += first[i]
        return prefix