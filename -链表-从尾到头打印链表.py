# 问题描述：从尾到头打印链表
# 模板：【1， 2， 3， 4， 5】

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ListFromTail(object):
    def __init__(self):
        pass

    #方法一：递归
    def list_from_tail(self, list_head):
        if list_head.next == None:
            print(list_head.val)
            return
        self.list_from_tail(list_head.next)
        print(list_head.val)

    #方法二：反转链表

if __name__ == "__main__":
    L = ListFromTail()

    head = ListNode(1)
    node1 = ListNode(3)
    node2 = ListNode(5)
    node3 = ListNode(2)
    node4 = ListNode(4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    L.list_from_tail(head)