# 问题描述
# 模板：

class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class LishClone(object):
    def __init__(self):
        pass

    def list_clone(self, head):
        if head == None:
            return None

        #第一步：复制单向链表
        pnext = head.next

        new_head = RandomListNode(head.label)
        new_pcur = new_head
        while pnext:
            new_pnext = RandomListNode(pnext.label)
            new_pcur.next = new_pnext

            pnext = pnext.next
            new_pcur = new_pnext

        #第二步：遍历两个链表，确定随机节点
        p = head
        np = new_head
        while p:
            #print(p.label, np.label)
            if p.random == None:
                np.random = None
            else:
                find_random = new_head
                while find_random.label != p.random.label:
                    find_random = find_random.next
                np.random = find_random
            p = p.next
            np = np.next
        return new_head




if __name__ == "__main__":
    S = LishClone()

    node1 = RandomListNode(1)
    node2 = RandomListNode(2)
    node3 = RandomListNode(3)
    node4 = RandomListNode(4)
    node5 = RandomListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = None
    node1.random = node5
    node2.random = node4
    node3.random = node3
    node4.random = node2
    node5.random = node1



    new_head = S.list_clone(node1)
    while new_head:
        print(new_head.label, new_head.random.label)
        new_head = new_head.next