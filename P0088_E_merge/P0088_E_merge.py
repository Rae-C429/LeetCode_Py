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
                k-=1
            else:
                nums1[k] = nums2[j]
                j-=1
                k-=1
        # 如果還有nums2[j] <nums1[i]
        while j>=0:
                nums1[k] = nums2[j]
                k-=1
                j-=1
            

