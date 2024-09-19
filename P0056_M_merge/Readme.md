## 56. Merge Intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:\
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]\
Output: [[1,6],[8,10],[15,18]]\
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:\
Input: intervals = [[1,4],[4,5]]\
Output: [[1,5]]\
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

### Note:
- stack(先進後出)

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 創建堆疊
        stack = []
        intervals = sorted(intervals)
        # 將第一個子列壓入堆疊
        stack.append(intervals[0])
        for i in range(1,len(intervals)):
            # 當前[start,end]
            b1 = intervals[i][0]
            b2 = intervals[i][1]
            # stack中top[start,end]
            a1 = stack[-1][0]
            a2 = stack[-1][1]
            # 如果重疊
            if a2 >= b1:
                stack[-1][1] = max(a2, b2)
                # 要嘛用pop,不要用a2改!
            else:
                stack.append(intervals[i])
        return stack
```