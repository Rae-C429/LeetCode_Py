class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 創建虛擬頭節點
        dummyHead = ListNode(0)
        # 將指針指向虛擬頭
        current = dummyHead
        # 初始化進位
        carry = 0
        # 計算l1,l2節點相加值
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0

            sum = carry + x + y
            carry = sum // 10
            # 將計算出得值放入創建的節點
            current.next = ListNode(sum % 10)
            # 更新指針位置
            current = current.next

            # 前往l1,l2下一的節點
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if carry > 0:
            current.next = ListNode(carry)

        return dummyHead.next