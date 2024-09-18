## 21. Merge Two Sorted Lists

You are given the heads of two sorted linked lists list1 and list2.\
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.\
Return the head of the merged linked list.

Example 1:
![alt text](image-1.png)
Input: list1 = [1,2,4], list2 = [1,3,4]\
Output: [1,1,2,3,4,4]

Example 2:\
Input: list1 = [], list2 = []\
Output: []

Example 3:\
Input: list1 = [], list2 = [0]\
Output: [0]

### gpt建議:
- 虛頭節點
- 指針

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 創建一個ListNode用來儲存整理好的資料
        dummy = ListNode(0)
        current = dummy # 將指針指向虛頭
        # 比較兩個list中的值
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next 
            else:
                current.next = list2
                list2 = list2.next 
            current = current.next
        # 將 next 指向剩餘的list
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next
```