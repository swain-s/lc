# 问题描述：输入两棵树，判断B是否为A的子树，约定空树不是任何树的子树
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

class IsSubTree(object):
    def __init__(self):
        pass

    #方法一：递归
    def is_sub_tree(self, root_a, root_b):
        if root_b == None or root_a == None:
            return False

        def is_iqual_tree(root_a, root_b):
            if not root_b:
                return True
            if not root_a or root_a.val != root_b.val:
                return False
            return is_iqual_tree(root_a.left, root_b.left) and is_iqual_tree(root_a.right, root_b.right)

        return is_iqual_tree(root_a, root_b) or self.is_sub_tree(root_a.left, root_b) or self.is_sub_tree(root_a.right, root_b)


    #方法二：迭代
    #分析：不知道哪里出问题，未通过
    def is_sub_tree_(self, root_a, root_b):
        if root_b == None or root_a == None:
            return False

        stack = []
        cur = root_a
        while cur or len(stack) > 0:
            if cur:

                #start
                if cur.val == root_b.val:
                    cur_b = root_b
                    stack_b = []
                    while cur_b or len(stack_b) > 0:
                        if cur_b and cur:
                            print(cur_b.val, cur.val)
                            if cur_b.val == cur.val:
                                stack_b.append(cur_b)
                                stack.append(cur)
                                cur_b = cur_b.left
                                cur = cur.left
                            else:
                                return False
                        else:
                            cur_b = stack_b.pop()
                            cur = stack.pop()
                            cur_b = cur_b.right
                            cur = cur.right
                    return True
                #end

                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right
        return False


if __name__ == "__main__":
    S = IsSubTree()
    print(S.is_sub_tree(root, rootb))