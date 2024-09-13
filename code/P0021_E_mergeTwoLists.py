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
 
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next 
            else:
                current.next = list2
                list2 = list2.next 
            current = current.next
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return dummy.next