## 17. Letter Combinations of a Phone Number

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
![alt text](image-17.png)

Example 1:\
Input: digits = "23"\
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:\
Input: digits = ""\
Output: []

Example 3:\
Input: digits = "2"\
Output: ["a","b","c"]

### Note:
1. 使用dict
2. 利用雙迴圈，讓數字應到的值配對(x)
## gpt建議:
- 使用遞迴

```python
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
```