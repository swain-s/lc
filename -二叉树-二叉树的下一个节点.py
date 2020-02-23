# 问题描述：给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
# 模板：        7
#      3             10
#  1      5      9         12
#      4                       14
#

from a_bin_tree import root, tin_travel


class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


class NextOfInOrder(object):
    def __init__(self):
        pass

    def next_of_in_order(self, node):
        if node == None:
            return None


        stack = []
        cur = node
        while cur or len(stack)>0:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = cur.pop()
                if cur == node:

                cur = cur.right
        cur


if __name__ == "__main__":
    S = Solution()

if __name__ == "__main__":
    S = Solution()