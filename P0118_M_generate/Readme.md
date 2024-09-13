## 118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:\
Input: numRows = 5\
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:\
Input: numRows = 1\
Output: [[1]]

## Note:
1. 初始化一個包含一個數字1的列表 (ex: [1,1,1])
2. 利用前一行跟改list中間值(ex: [1,2,1])

## 注意：
1. 需要兩個list，一個用來初始化，一個用來以計算好的值

```python
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        pascal = []
        for i in range(numRows):
            row = [1]*(i+1)
            for j in range(1,i):
                row[j] =  pascal[i-1][j-1]+pascal[i-1][j]
            pascal.append(row)
        return pascal
```