class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Optional 是 typing 模塊中的一个泛型類型，表示某個變量要麽是指定的類型（這裡是 ListNode），要麽是 None。
        # 創建一個虛擬的節點頭
        dummyHead = ListNode(0)
        # 創建指針只先目前位置
        current = dummyHead
        # 初始化進位
        carry = 0
        # 計算l1,l2的值
        while l1 is not None or l2 is not None:
            x = l1.val if is not None else 0
            y = l2.val if is not None else 0
            sum = x + y + carry
            # 進位計算
            carry = carry // 10
            # 將計算出的答案增加至下一個節點
            current.next = ListNode(sum % 10)
            current = current.next
            # 前往l1,l2下一節點
            if l1 is not None:
                l1 = l1.next 
            if l2 is not None:
                l2 = l2.next

            if carry > 0:
                current.next = ListCode(carry)
                
            return dummyHead.next