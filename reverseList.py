class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList1(self, head: ListNode) -> ListNode:
        """解法一：双指针法  """
        cur = head
        pre = None
        while cur:
            temp = cur.next  # head用于保存下一个结点
            cur.next = pre   # 反转链表操作
            pre = cur        #先将cur的值传递给pre，再移动cur
            cur = temp
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        """解法二：递归法，和双指针法相同"""
        def reverse(cur, pre):
            if cur == None:
                return pre
            temp = cur.next
            cur.next = pre
            return reverse(temp, cur)
        return reverse(head, None)

