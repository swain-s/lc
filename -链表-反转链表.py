# 问题描述：反转链表, 返回新头部
# 模板：【1， 2， 3， 4， 5】

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ReverseList(object):
    def __init__(self):
        pass

    # 方法一：递归
    def reverse_list(self, head):
        if head == None:
            return None
        elif head.next == None:
            return head
        elif head.next.next == None:
            head.next.next = head
            head.next = None
            return head.next

        def reverse_list(phead, pcur, pnext):
            if pnext.next == None:
                pnext.next = pcur
                return pnext
            p = reverse_list(phead, pcur.next, pnext.next)
            pnext.next = pcur

            if pcur == phead:
                phead.next = None
            return p

        return reverse_list(head, head, head.next)

    #方法二：三指针法
    # 分析：previous, pcurrent, pnext(为了顺序定位)


if __name__ == "__main__":
    L = ReverseList()

    head = ListNode(1)
    node1 = ListNode(3)
    node2 = ListNode(5)
    node3 = ListNode(2)
    node4 = ListNode(4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    new_head = L.reverse_list(head)
    pcur = new_head
    while pcur:
        print(pcur.val)
        pcur = pcur.next
