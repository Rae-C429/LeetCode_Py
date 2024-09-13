class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 注意digits為空
        if not digits:
            return []
        # 創造 key-value
        digToLet = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
                    }
        # ref: gpt
        def backtrack(index, path):
            if index == len(digits):
                combination.append(''.join(path))
                return

            letters = digToLet[digits[index]]
            for letter in letters:
                path.append(letter)
                backtrack(index+1, path)
                path.pop()
        
        combination = []
        backtrack(0, [])
        return combination

