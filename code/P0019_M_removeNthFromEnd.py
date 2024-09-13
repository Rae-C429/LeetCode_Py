# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 創建虛擬頭節點（如果要刪除的是第一個節點）
        dummy = ListNode(0)
        dummy.next = head
        # 初始化指針 slow、fast 。
        slow = dummy
        fast = dummy
        # slow 與 fast 相距 n 步，slow為被刪除的前一個(寫進 while 迴圈裡)
        for i in range(n+1):
                fast = fast.next        
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next

        return dummy.next