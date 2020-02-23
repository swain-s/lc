# 问题描述：输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向
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

class TreeToList(object):
    def __init__(self):
        pass

    #辅助函数：查找二叉树或者双向链表（输入为任一节点）的最大节点
    def find_max(self, root):
        if root == None:
            return None
        if root.right == None:
            return root
        return self.find_max(root.right)

    # 辅助函数：查找二叉树或者双向链表（输入为任一节点）的最小节点
    def find_min(self, root):
        if root == None:
            return None
        if root.left == None:
            return root
        return self.find_min(root.left)

    #辅助函数：自己调试的时候用
    def print_node(self, node1, node2):
        if not node1 and not node2:
            return [-1, -1]
        if node1 and node2:
            return [node1.val, node2.val]
        if node1 and not node2:
            return [node1.val, -1]
        return [-1, node2.val]

    #方法一：按后续遍历顺序
    def tree_to_list(self, root):
        if root == None:
            return
        #if root.left == None and root.right == None:
            #return

        self.tree_to_list(root.left)
        self.tree_to_list(root.right)

        print(root.val, end=":   ")
        print(self.print_node(root.left, root.right), end="        --->    ")

        le_node = self.find_max(root.left)
        root.left = le_node
        if le_node:
            le_node.right = root

        ri_node = self.find_min(root.right)
        root.right = ri_node
        if ri_node:
            ri_node.left = root

        print(self.print_node(le_node, ri_node))

        return root

if __name__ == "__main__":
    S = TreeToList()
    r = S.tree_to_list(root)
    rr = r
    while r:
        print(r.val)
        r = r.right
    while rr:
        print(rr.val)
        rr = rr.left
