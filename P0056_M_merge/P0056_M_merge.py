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