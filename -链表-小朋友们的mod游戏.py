# 问题描述：n个小朋友，0到n-1,数为m， 0到m-1, m-1出列
# 模板：
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class ModGame(object):
    def __init__(self):
        pass

    #辅助函数：环形链表的长度（不带头结点）
    def circle_len(self, head):
        if head == None:
            return 0
        if head.next == None:
            return 1

        fir_value = head.val
        cnt = 1
        cur = head.next
        while cur:
            if cur.val == fir_value:
                return cnt
            cnt += 1
            cur = cur.next

    #辅助函数：遍历环形链表（不带头结点）
    def circle_travel(self, head):
        if head == None:
            return None

        vals = []
        vals.append(head.val)
        if head.next == None:
            return vals

        fir_value = head.val
        cur = head.next
        while cur and cur.val != fir_value:
            vals.append(cur.val)
            cur = cur.next
        return vals

    def mod_game(self, n, m):
        if n <= 0:
            return -1
        #构造环形链表
        head = ListNode(-1)
        cur = head
        for num in range(n):
            node = ListNode(num)
            cur.next = node
            cur = cur.next
        new_head = head.next
        cur.next = new_head

        while self.circle_len(new_head) > 1:
            print(self.circle_travel(new_head))
            out = new_head
            for cnt in range(m-2):
                out = out.next
            out.val = out.next.val
            out.next = out.next.next
            new_head = out.next

        return new_head.val


if __name__ == "__main__":
    S = ModGame()

    head = ListNode(1)
    node1 = ListNode(3)
    node2 = ListNode(5)
    node3 = ListNode(2)
    node4 = ListNode(4)
    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1

    #print(S.circle_len(node1))
    print(S.mod_game(10, 3))