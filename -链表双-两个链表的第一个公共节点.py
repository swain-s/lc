# 问题描述：两个链表的第一个公共节点
# 模板：[1, 3, 5, 7, 9] [2, 4, 6, 8, 10]

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class FirstCommonNode(object):
    def __init__(self):
        pass

    #方法二：hash表
    #方法一：求出长度差值
    def first_common_node(self, head1, head2):
        if head1 == None or head2 == None:
            return None

        len1 = 0
        len2 = 0
        cur1 = head1
        cur2 = head2
        while cur1:
            len1 += 1
            cur1 = cur1.next
        while cur2:
            len2 += 1
            cur2 = cur2.next

        if len1 >= len2:
            k = len1 - len2
            long = head1
            short = head2
        else:
            k = len2 - len1
            long = head2
            short = head1

        cnt = 0
        while long:
            if cnt == k:
                break
            cnt += 1
            long = long.next

        while long and short:
            if long == short:
                print("find it", long.val)
                return long
            long = long.next
            short = short.next

        return None

if __name__ == "__main__":
    L = FirstCommonNode()

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
    #node33 = ListNode(10)
    #node44 = ListNode(12)
    head2.next = node22
    #node11.next = node22
    node22.next = node3

    common_node = L.first_common_node(head1, head2)
    print(common_node.val)

