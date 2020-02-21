# 问题描述：链表倒数第K个节点
# 模板：【1， 2， 3， 4， 5】

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class ListKFromTail(object):
    def __init__(self):
        pass

    # 方法一：递归中定位（存在问题，pass）
    # 分析：复杂
    def list_k_from_tail(self, list_head, k):
        if list_head == None:
            return False

        llen = 1
        pcnt = list_head
        while pcnt.next != None:
            pcnt = pcnt.next
            llen += 1

        def list_from_tail(head, k_, cnt, llen_):
            if head.next == None:
                if llen_ - cnt == k_:
                    print("last", llen, cnt, k_)
                    print(head.val)
                return

            cnt += 1
            list_from_tail(head.next, k_, cnt, llen_)
            if llen_ - cnt == k_:
                print("not", llen_, cnt, k_)
                print(head.val)
                return
            return
        list_from_tail(list_head, k, 0, llen-1)

    # 方法二：先指针和后指针
    def list_k_from_tail_(self, head, k):
        fir = head
        sec = head
        for i in range(k):
            if fir.next == None:
                return None
            fir = fir.next
        while sec:
            if fir.next == None:
                return sec.val
            sec = sec.next
            fir = fir.next


if __name__ == "__main__":
    L = ListKFromTail()

    head = ListNode(1)
    node1 = ListNode(3)
    node2 = ListNode(5)
    node3 = ListNode(2)
    node4 = ListNode(4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    L.list_k_from_tail(head, 2)

    print(L.list_k_from_tail_(head, 0))