# 问题描述：[路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径] 输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径
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

class FindPath(object):
    def __init__(self):
        pass

    #方法一：减法递归
    #分析：递归不需要引入新的参数
    def find_path(self, root, expect_sum):
        if root == None:
            return []

        remain = expect_sum - root.val
        if remain == 0 and root.left == None and root.right == None:
            return [[root.val]]
        if remain <= 0:
            return []
        if remain > 0:
            le = self.find_path(root.left, remain)
            ri = self.find_path(root.right, remain)

            path = le + ri
            for arr in path:
                if len(arr) > 0:
                    arr.insert(0, root.val)
            return path


    #方法二：加法递归（pass）-- 未完全通过，找不出原因
    #分析：需要维护一个栈和当前的和，比较复杂
    def find_path_(self, root, expect_sum):
        def new_find_path(root, expect_sum, cur_stack, cur_sum, output):
            if root == None:
                return
            print(root.val ,[node.val for node in cur_stack], cur_sum, " ----------", output)

            if root.val == expect_sum:
                output.append([root.val])
                cur_stack = []
                cur_sum = 0
            elif cur_sum + root.val > expect_sum:
                cur_stack = []
                cur_sum = 0
            elif cur_sum + root.val == expect_sum:
                cur_stack.append(root)

                find_arr = []
                for node in cur_stack:
                    find_arr.append(node.val)
                output.append(find_arr)

                cur_stack = []
                cur_sum = 0
            elif cur_sum + root.val < expect_sum:
                cur_stack.append(root)
                cur_sum += root.val
            stack = cur_stack
            sum = cur_sum
            new_find_path(root.left, expect_sum, cur_stack, cur_sum, output)
            new_find_path(root.right, expect_sum, stack, sum, output)

        output = []
        new_find_path(root, expect_sum, [], 0, output)

        if len(output) < 2:
            return output

        len_output = []
        for arr in output:
            len_output.append(len(arr))
        for j in range(0, len(len_output)):
            last = (len(len_output) - 1) - j
            for i in range(0, last):
                if len_output[i] < len_output[i + 1]:
                    temp = len_output[i]
                    len_output[i] = len_output[i + 1]
                    len_output[i + 1] = temp

                    temp = output[i]
                    output[i] = output[i + 1]
                    output[i + 1] = temp

        return output

    #测试
    def test(self):
        out_put = []
        arr = []
        for i in range(10):
            for j in range(i+1):
                arr.append(j)
            out_put.append(arr)
            arr = []
        return out_put



if __name__ == "__main__":
    S = FindPath()
    #print(S.test())
    print(S.find_path(root, 19))