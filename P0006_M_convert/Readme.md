## 6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N\
A P L S I I G\
Y   I   R\
And then read line by line: "PAHNAPLSIIGYIR"\
Write the code that will take a string and make this conversion given a number of rows:\
string convert(string s, int numRows);
 
Example 1:\
Input: s = "PAYPALISHIRING", numRows = 3\
Output: "PAHNAPLSIIGYIR"

Example 2:\
Input: s = "PAYPALISHIRING", numRows = 4\
Output: "PINALSIGYAHRPI"\
Explanation:\
P     I    N\
A   L S  I G\
Y A   H R\
P     I

Example 3:\
Input: s = "A", numRows = 1\
Output: "A"

### gpt建議:
- 建立有numRows個子列表的列表
- 填列表，注意方方向

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows>len(s):
            return s
        # 創建一個大小為 numRows 的列表
        z1 = [""]*numRows
        # 方向
        j = 1
        #當前的行號
        current_row = 0
        for i in s:
            z1[current_row]+=i
            if current_row == numRows-1:
                j = -1 
            elif current_row == 0:
                j = 1 
            current_row += j
        return ''.join(z1)         
```