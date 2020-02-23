# 问题描述：实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
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

class PrintTree(object):
    def __init__(self):
        pass

    def print_tree(self, root):
        if root == None:
            return []
        out_put = []
        def new_print_tree(node_stack, layer_cnt, output):
            if node_stack == None or node_stack == []:
                return output

            next_stack = []
            print_stack = []
            # 从左到右
            if layer_cnt % 2 == 1:
                for node in node_stack:
                    print_stack.append(node.val)
                    if node.left:
                        next_stack.append(node.left)
                    if node.right:
                        next_stack.append(node.right)
                output.append(print_stack)
            # 从右到左
            elif layer_cnt % 2 == 0:
                for node in node_stack:
                    if node.left:
                        next_stack.append(node.left)
                    if node.right:
                        next_stack.append(node.right)
                while node_stack != []:
                    print_stack.append(node_stack.pop().val)
                output.append(print_stack)
            return new_print_tree(next_stack, layer_cnt + 1, output)

        return new_print_tree([root], 1, out_put)


if __name__ == "__main__":
    S = PrintTree()
    print(S.print_tree(root))