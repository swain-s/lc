# 问题描述
# 模板：

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class DelRepeateNode(object):
    def __init__(self):
        pass

    #递归实现
    def del_repeate_node(self, head):
        

    #重复的全删了(pass)
    def del_repeate_node_(self, head):
        if head == None or head.next == None:
            return head
        if head.val == head.next.val:
            return head.next.next

        pre = head
        cur = head.next
        while cur:
            repeat_signal = 0
            while cur and cur.next and cur.val == cur.next.val:
                repeat_signal = 1
                cur = cur.next

            if repeat_signal == 0:
                pre = cur
                cur = cur.next
            else:
                pre.next = cur.next
                cur = pre
        return head


    #保留重复中的一个
    def del_repeate_node_1(self, head):
        if head == None or head.next == None:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

if __name__ == "__main__":
    S = DelRepeateNode()

    head = ListNode(1)
    node1 = ListNode(3)
    node2 = ListNode(5)
    node3 = ListNode(5)
    node4 = ListNode(4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    root = S.del_repeate_node(head)
    while root:
        print(root.val)
        root = root.next
