import copy
class Node:
    """单链表结点"""
    def __init__(self,info):
        self.info = info
        self.next = None
class SingleLinkList:
    """单链表表头"""
    def __init__(self):
        self.next = None

    def is_empty(self):
        """判断链表是否为空"""
        return self.next is None

    def length(self):
        """返回链表长度"""
        cur = self.next
        count = 0
        while cur is not None:
            cur = cur.next
            count += 1
        return count

    def append(self,re):
        node = Node(re)
        cur = self.next
        while cur.next is not None:
            cur = cur.next
        cur.next = node


if __name__ == "__main__":
    x = SingleLinkList()
    node1 = Node(1)
    node2 = Node(2)
    x.next = node1
    node1.next = node2
    print(x.length())
    x.append(3)
    print(x.length())




