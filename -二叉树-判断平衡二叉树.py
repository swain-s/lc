# 问题描述：输入一棵二叉树，判断该二叉树是否是平衡二叉树。
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

class IsAVLTree(object):
    def __init__(self):
        pass

    #辅助函数：返回两个整数中的较大者
    def max_path(self, path1, path2):
        return path1 if path1 >= path2 else path2

    #方法一：后序遍历递归
    def is_avl_tree(self, root):
        if root == None:
            return True #剑指Offer要求返回True

        bool = [True]

        def new_is_avl_tree(root, bool):
            if root == None:
                return 0
            if root.left == None and root.right == None:
                return 1

            le_path = new_is_avl_tree(root.left, bool)
            ri_path = new_is_avl_tree(root.right, bool)
            sub = le_path - ri_path if le_path >= ri_path else ri_path - le_path
            if sub > 1:
                bool[0] = False
            return self.max_path(le_path, ri_path) + 1

        new_is_avl_tree(root, bool)
        return bool[0]

if __name__ == "__main__":
    S = IsAVLTree()
    print(S.is_avl_tree(root))