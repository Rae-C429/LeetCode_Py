class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        stack = []
        stack.append(-1)
        maxLen = 0
        for i in range(n):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxLen = max(maxLen, i - stack[-1])
        return maxLen