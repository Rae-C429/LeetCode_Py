## 83. Remove Duplicates from Sorted List
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

Example 1:\
![alt text](image-2.png)
Input: head = [1,1,2]\
Output: [1,2]

Example 2:\
![alt text](image-3.png)
Input: head = [1,1,2,3,3]\
Output: [1,2,3]

### Note:
- 利用指針current，當相鄰兩束相同時要跳過，不同時指針向下過移動。

### 解答
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        current = head
        if current is None:
            return head
            
        while current.next:
            if current.next.val  == current.val:
                current.next = current.next.next

            else:
                current = current.next
        return head
```