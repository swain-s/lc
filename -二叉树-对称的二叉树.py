# 问题描述：判断一颗二叉树是不是对称的。注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。
# 模板：        7
#      3             10
#  1      5      9         12
#      4                       14
#

from a_bin_tree import root, tin_travel, rootb

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class IsSymmetricalTree(object):
    def __init__(self):
        pass

    def is_symmetrical_tee(self, root):
        if root == None:
            return True
        if root.left == root.right == None:
            return True

        def is_left_mirror_right(lroot, rroot):
            if rroot == lroot == None:
                return True
            if lroot == None or rroot == None or lroot.val != rroot.val:
                return False
            return is_left_mirror_right(lroot.left, rroot.right) and is_left_mirror_right(lroot.right, rroot.left)

        return is_left_mirror_right(root.left, root.right)


if __name__ == "__main__":
    S = IsSymmetricalTree()
    print(S.is_symmetrical_tee(root))