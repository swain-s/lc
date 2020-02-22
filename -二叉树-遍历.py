# 问题描述：二叉树的前序、中序、后续和层次遍历
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

class BinTreeTreveral(object):
    def __init__(self):
        pass

    def pre_order_traveral(self, root, output):
        if root == None:
            return
        output.append(root.val)
        self.pre_order_traveral(root.left, output)
        self.pre_order_traveral(root.right, output)

    def in_order_traveral(self, root, output):
        if root == None:
            return
        self.in_order_traveral(root.left, output)
        output.append(root.val)
        self.in_order_traveral(root.right, output)

    #中序遍历的迭代版本
    def in_order_traveral_stack(self, output):

    def post_order_traveral(self, root, output):
        if root == None:
            return
        self.in_order_traveral(root.left, output)
        self.in_order_traveral(root.right, output)
        output.append(root.val)


    def level_order_traveral(self, root):
        pass

if __name__ == "__main__":
    S = BinTreeTreveral()
    pre_arr = []
    S.pre_order_traveral(root, pre_arr)
    print(pre_arr)

    in_arr = []
    S.in_order_traveral(root, in_arr)
    print(in_arr)

    post_arr = []
    S.post_order_traveral(root, post_arr)
    print(post_arr)
