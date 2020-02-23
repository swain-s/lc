# 问题描述：输入一棵二叉树，求该树的深度
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

class TreePath(object):
    def __init__(self):
        pass

    #辅助函数：返回两个整数中的较大者
    def max_path(self, path1, path2):
        return path1 if path1 >= path2 else path2

    def tree_path(self, root):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1

        return self.max_path(self.tree_path(root.left), self.tree_path(root.right)) + 1


if __name__ == "__main__":
    S = TreePath()
    print(S.tree_path(root))