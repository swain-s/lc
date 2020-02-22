# 问题描述：
# 模板：        7
#      3             10
#  1      5      9         12
#      4                       14
#

# 结果：        7
#      10             3
#   12    9      5         11
# 14                   4
#

from a_bin_tree import root, tin_travel

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MirrorTree(object):
    def __init__(self):
        pass

    def mirror_tree(self, root):
        if root == None:
            return

        self.mirror_tree(root.left)
        self.mirror_tree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        return root


if __name__ == "__main__":
    S = MirrorTree()
    #tin_travel(root)
    new_root = S.mirror_tree(root)
    tin_travel(new_root)
