# 问题描述：合并两个有序链表
# 模板：[1, 3, 5, 7, 9] [2, 4, 6, 8, 10]

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Merger(object):
    def __init__(self):
        pass

    # 
    def merger(self, head1, head2):
        if head1 == None and head2 == None:
            return None
        elif head1 == None:
            return head2
        elif head2 == None:
            return head1

        (small_head, big_head) = (head1, head2) if head1.val <= head2.val else (head2, head1)

        new_head = ListNode(0)
        pcur = new_head
        while small_head and big_head and small_head.val <= big_head.val:
            #print("1 < 2", small_head.val, big_head.val)
            pcur.next = small_head
            pcur = pcur.next
            small_head = small_head.next
            while small_head and big_head and small_head.val > big_head.val:
                #print("1 >> 2", small_head.val, big_head.val)
                pcur.next = big_head
                pcur = pcur.next
                big_head = big_head.next

        while small_head:
            pcur.next = small_head
            pcur = pcur.next
            small_head = small_head.next
        while big_head:
            pcur.next = big_head
            pcur = pcur.next
            big_head = big_head.next

        return new_head.next




if __name__ == "__main__":
    L = Merger()

    head1 = ListNode(1)
    node1 = ListNode(3)
    node2 = ListNode(5)
    node3 = ListNode(7)
    node4 = ListNode(9)
    head1.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    head2 = ListNode(2)
    node11 = ListNode(4)
    node22 = ListNode(8)
    node33 = ListNode(10)
    node44 = ListNode(12)
    head2.next = node11
    node11.next = node22
    node22.next = node33
    node33.next = node44

    new_head = L.merger(head1, head2)
    pcur = new_head
    while pcur:
        print(pcur.val)
        pcur = pcur.next
