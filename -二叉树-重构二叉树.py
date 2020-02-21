# 问题描述：已知：先序遍历，中序遍历  --> 重构二叉树
# 模板：先序【1， 2， 4， 7, 3， 5， 6， 8】； 中序【4， 7， 2 ，1， 5， 3 ，8， 6】

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


if __name__ == "__main__":
    S = RebuildBintree()
    root = S.rebuild_bintree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
    S.tin_travel(root)
