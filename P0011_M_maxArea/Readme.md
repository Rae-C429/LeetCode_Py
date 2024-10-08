## 11. Container With Most Water
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:\
![alt text](image-5.png)\
Input: height = [1,8,6,2,5,4,8,3,7]\
Output: 49\
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:\
Input: height = [1,1]\
Output: 

### Note:
- 利用雙指針
- 將左右指針寬度設為最寬
- 犧牲寬度，將最矮的必替換，看看水量能否提升

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0

        while left < right:
            now = (right - left) * min(height[left], height[right])
            if area < now:
                area = now
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return area
```