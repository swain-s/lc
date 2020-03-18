# 问题描述
# 模板：

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class FindEntryNode(object):
    def __init__(self):
        pass

    #辅助函数：找到环的长度
    def lenth_of_circle(self, head):
        if head == None or head.next == None:
            return 0
        one_stp = two_stp = head
        max_depth = 50
        while one_stp.next and two_stp.next.next:
            max_depth -= 1
            if max_depth < 0:
                exit(-1)

            one_stp = one_stp.next
            two_stp = two_stp.next.next

            if one_stp == two_stp:
                cnt = 1
                while one_stp.next:
                    max_depth -= 1
                    if max_depth < 0:
                        exit(-1)

                    one_stp = one_stp.next
                    if one_stp == two_stp:
                        return cnt
                    cnt += 1

    #方法一：hash表（节点值不相等）
    #方法二：一：快指针 + 慢指针 找到环的长度， 二,先指针 + 慢指针 找到环的入口
    def find_entry_node(self, head):
        if head == None or head.next == None:
            return None

        circle_len = self.lenth_of_circle(head)

        fir_stp = sec_stp = head
        for cnt in range(circle_len):
            if sec_stp.next:
                sec_stp = sec_stp.next

        while fir_stp and sec_stp:
            if fir_stp == sec_stp:
                return fir_stp
            fir_stp = fir_stp.next
            sec_stp = sec_stp.next



if __name__ == "__main__":
    S = FindEntryNode()

    head = ListNode(1)
    node1 = ListNode(3)
    node2 = ListNode(5)
    node3 = ListNode(2)
    node4 = ListNode(4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    print(S.find_entry_node(head).val)