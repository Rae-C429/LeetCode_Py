class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None:
            return ""
        # 利用第一個字串作為比較對象
        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in (strs[1:]):
                if i >= len(s) or s[i]!= char:
                    return strs[0][:i]
        return strs[0]
        strs = sorted(strs)
        prefix = ""
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first),len(last))):
            if first[i] != last[i]:
                return prefix 
            prefix += first[i]
        return prefix