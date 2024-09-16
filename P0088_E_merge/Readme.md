## 88. Merge Sorted Array

Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3\
Output: [1,2,2,3,5,6]\
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements\ coming from nums1.

Example 2:\
Input: nums1 = [1], m = 1, nums2 = [], n = 0\
Output: [1]\
Explanation: The arrays we are merging are [1] and [].\
The result of the merge is [1].

Example 3:\
Input: nums1 = [0], m = 0, nums2 = [1], n = 1\
Output: [1]\
Explanation: The arrays we are merging are [] and [1].\
The result of the merge is [1].\
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

### Note:
1. 使用三個指針
2. 從後面開始比較

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 指向nums1最後一個元素
        i = m - 1
        # 指向nums2最後一個元素
        j = n - 1
        # 指向nums1最後一個索引
        k = m + n - 1

        # 比較大小
        while j>=0 and i>=0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i-=1
            else:
                nums1[k] = nums2[j]
                j-=1
            k-=1
        # 如果還有nums2[j] <nums1[i]
        while j>=0:
                nums1[k] = nums2[j]
                k-=1
                j-=1
```