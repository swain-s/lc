# 问题描述：从上往下，分层打印二叉树，每层从左往右
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

class TopToBottom(object):
    def __init__(self):
        pass

    #方法一：分层
    #分析：空间复杂度：越往底层，空间复杂度越高
    def top_to_bottom(self, root):
        def layer(cur_layer):
            if len(cur_layer) == 0:
                return

            next_layer = []
            for node in cur_layer:
                print(node.val, end=", ")
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            layer(next_layer)

        cur_layer = [root]
        layer(cur_layer)


if __name__ == "__main__":
    S = TopToBottom()
    S.top_to_bottom(root)