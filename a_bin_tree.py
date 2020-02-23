#该文件为一个二叉树示例（通过重构那题得到的二叉树）

# 问题描述：已知：先序遍历，中序遍历  --> 重构二叉树
# 模板：        7
#      3             10
#  1      5      9         12
#      4                       14
#

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class RebuildBintree(object):
    def __init__(self):
        pass

    #辅助函数：获取元素在数组中的位置
    def pos_in_arr(self, arr, num):
        if len(arr) == 0:
            return None
        for i in range(len(arr)):
            if arr[i] == num:
                return i

    #辅助函数：二叉树：中序遍历
    def tin_travel(self, root):
        if root == None:
            return

        self.tin_travel(root.left)
        print(root.val)
        self.tin_travel(root.right)

    def rebuild_bintree(self, pre_arr, tin_arr):
        if len(pre_arr) != len(tin_arr):
            return None
        if not pre_arr:
            return None

        root = pre_arr[0]
        root_node = TreeNode(root)

        self.pos_in_arr(tin_arr, root)
        tin_left = tin_arr[:self.pos_in_arr(tin_arr, root)]
        tin_right = tin_arr[self.pos_in_arr(tin_arr, root)+1:]

        pre_left = pre_arr[1:self.pos_in_arr(tin_arr, root)+1]
        pre_right = pre_arr[self.pos_in_arr(tin_arr, root)+1:]

        left_node = self.rebuild_bintree(pre_left, tin_left)
        right_node = self.rebuild_bintree(pre_right, tin_right)
        root_node.left = left_node
        root_node.right = right_node

        return root_node

S = RebuildBintree()
root = S.rebuild_bintree([7, 3, 1, 5, 4, 10 ,9, 12, 14], [1, 3, 4, 5, 7, 9, 10, 12, 14])
rootb = S.rebuild_bintree([3, 1, 5], [1, 3, 5])


def tin_travel(root):
    if root == None:
        return

    tin_travel(root.left)
    print(root.val, end=", ")
    tin_travel(root.right)

