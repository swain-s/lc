# 问题描述：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。假设输入的数组的任意两个数字都互不相同。
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

class IsSquenceOfBST(object):
    def __init__(self):
        pass

    #辅助函数：输入：后续遍历序列，输出：左子树序列和右子树序列
    def find_divide(self, sequence):
        left = []
        right = []
        if sequence == None or len(sequence) == 0:
            return left, right

        for cur in range(len(sequence)-1):
            if sequence[cur] < sequence[-1]:
                left.append(sequence[cur])
            else:
                right = sequence[cur:len(sequence)-1]
                break
        return left, right

    #方法一：递归
    def is_sequence_of_BST(self, sequence):
        if not sequence or len(sequence) == 0:
            return False

        #带递归的终止条件
        def new_is_sequence_of_BST(sequence):
            if len(sequence) == 0 or not sequence:
                return True

            left, right = self.find_divide(sequence)
            for num in right:
                if num <= sequence[-1]:
                    return False

            return new_is_sequence_of_BST(left) and new_is_sequence_of_BST(right)

        return new_is_sequence_of_BST(sequence)


if __name__ == "__main__":
    S = IsSquenceOfBST()
    print(S.is_sequence_of_BST([1, 3, 4, 5, 9, 10, 12, 14, 7]))