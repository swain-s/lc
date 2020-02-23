# 问题描述：序列化和反序列化二叉树
# 二叉树序列化：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
#              序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过
#              某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。
# 二叉树反序列化：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。
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

class SerializeTree(object):
    def __init__(self):
        pass

    #方法二：层次遍历
    def serialize_tree(self, root):
        if root == None:
            return []
        result = []
        result.append([str(root.val) + "!"])
        def new_serialize_tree(node_stack, output):
            if node_stack == None or node_stack == []:
                return output
            next_stack = []
            string_stack = []
            none_cnt = 0
            # 从左到右
            for node in node_stack:
                if node == None:
                    string_stack.append("#!")
                    string_stack.append("#!")
                    next_stack.append(None)
                    next_stack.append(None)
                else:
                    none_cnt += 1
                    if node.left:
                        string_stack.append(str(node.left.val) + "!")
                        next_stack.append(node.left)
                    else:
                        string_stack.append("#!")
                        next_stack.append(None)
                    if node.right:
                        string_stack.append(str(node.right.val) + "!")
                        next_stack.append(node.right)
                    else:
                        string_stack.append("#!")
                        next_stack.append(None)
            if none_cnt > 0:
                output.append(string_stack)
                return new_serialize_tree(next_stack, output)
            else:
                return output
        return new_serialize_tree([root], result)

    #方法二：层次遍历
    def deserialize_tree(self, string):
        if string == None:
            return None
        if len(string) == 1:
            root = self.get_int(string[0][0])
            return root
        for i in range(len(string)-1):
            for j in range(string[i]):
                root = self.get_int(string[i][j])
        pass

    #方法一：中序遍历，行不通，pass
    def serialize_tree_(self, root):
        result = []
        def in_order_traveral(root, result):
            if root == None:
                result.append("#!")
                return
            in_order_traveral(root.left, result)
            result.append(str(root.val) + "!")
            in_order_traveral(root.right, result)
        in_order_traveral(root, result)
        return result

    #辅助函数，从序列化字符串中提取整数并创建TreeNode
    def get_int(self, string):
        if string == "#!":
            return None
        elif len(string) < 2:
            return None
        elif len(string) > 1:
            num = int(string[0:len(string)-1])
            tree_node = TreeNode(num)
            return tree_node
        return None

    #方法一：pass
    def deserialize_tree_(self, string):
        if string == None:
            return None

        def bin_tree_build(string_arr, le, ri):
            #print(string_arr[le:ri+1])
            if ri - le < 3:
                return None
            elif len(string_arr) == 3:
                root = self.get_int(string_arr[1])
                if root == None:
                    return None
                left = self.get_int(string_arr[0])
                right = self.get_int(string_arr[2])
                root.left = left
                root.right = right
                return root
            elif len(string_arr) > 3:
                pos_mid = int(le + (ri - le) / 2)
                pos_le = int(le + (pos_mid-1 - 0) / 2)
                pos_ri = int(pos_mid+1 + (ri - pos_mid -1))
                root = self.get_int(string_arr[pos_mid])
                if root == None:
                    return None
                left = self.get_int(string_arr[pos_le])
                right = self.get_int(string_arr[pos_ri])
                root.left = left
                root.right = right

                bin_tree_build(string_arr, le, pos_mid-1)
                bin_tree_build(string_arr, pos_mid+1, ri)

                return root
            else:
                return None
        return bin_tree_build(string, 0, len(string)-1)



if __name__ == "__main__":
    S = SerializeTree()
    string = S.serialize_tree(root)
    print(string)
    print(len(string))