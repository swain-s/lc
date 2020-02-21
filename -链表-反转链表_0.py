# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

# 1 - 2 - 3 - 4 - 5 -6
# 3 - 2

arr = [1, 3, 5 ,7, 9]
lis = []
for i in arr:
    node = ListNode(i)
    lis.append(node)
for i in range(len(arr)-1):
    lis[i].next = lis[i+1]

def tra_l(head):
    cur = head
    while(True):
        print(cur.val)
        if(cur.next == None):
            return 0
        cur = cur.next

#tra_l(lis[0])

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode == None or listNode.next == None:
            return listNode
        your = listNode
        cur = listNode.next

        while (True):
            if cur.next.next == None:
                cur.next = your
                return cur.next
            my = cur.next.next
            cur.next.next = your
            your = my

    def digui(self, listNode):
        def recurse(head, newhead):  # 递归，head为原链表的头结点，newhead为反转后链表的头结点
            if head is None:
                return
            if head.next is None:
                newhead = head
            else:
                newhead = recurse(head.next, newhead)
                head.next.next = head
                head.next = None
            return newhead

        return recurse(listNode, listNode.next)

S = Solution()
#newhead = S.printListFromTailToHead(lis[0])
newhead = S.digui(lis[0])
tra_l(newhead)