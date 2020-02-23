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

        #有右子树，返回右子树的中序遍历的第一个节点
        if node.right:
            stack = []
            cur = node.right
            while cur or len(stack) > 0:
                if cur:
                    stack.append(cur)
                    cur = cur.left
                else:
                    tar_ndoe = stack.pop()
                    return tar_ndoe


        #无右子树，无双亲节点：返回None
        #无右子树，自己是双亲的左节点：返回双亲节点
        #无右子树, 自己是双亲的右节点，找到第一个祖先节点其双亲节点的左节点，返回该祖先的双亲（在自己右边的节点）
        if node.right == None:
            if node.next == None:
                return None
            elif node.next and node.next.left == node:
                return node.next
            elif node.next and node.next.right == node:
                cur = node.next
                while cur:
                    if cur.next and cur.next.left == cur:
                        return cur.next
                    cur = cur.next
                return None

if __name__ == "__main__":
    S = NextOfInOrder()
    print(S.next_of_in_order(root).val)
