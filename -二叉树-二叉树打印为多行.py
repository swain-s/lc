# 问题描述：从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
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
        def new_print_tree(node_stack, output):
            if node_stack == None or node_stack == []:
                return output
            next_stack = []
            print_stack = []
            # 从左到右
            for node in node_stack:
                print_stack.append(node.val)
                if node.left:
                    next_stack.append(node.left)
                if node.right:
                    next_stack.append(node.right)
            output.append(print_stack)

            return new_print_tree(next_stack, output)

        return new_print_tree([root] , out_put)


if __name__ == "__main__":
    S = PrintTree()
    print(S.print_tree(root))