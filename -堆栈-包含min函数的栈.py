# 问题描述:实现一个栈，包含min函数，（min函数的时间复杂度为1）
# 模板：

class MyStack(object):
    def __init__(self):
        self.stack = []
        self.min_num = None

    def push(self, node):
        self.stack.append(node)
        if len(self.stack) == 1:
            self.min_num = node
        else:
            if node < self.min_num:
                self.min_num = node

    def pop(self):
        #self.stack.pop()
        if len(self.stack) > 1:
            if self.stack[-1] == self.min_num:
                self.min_num = self.stack[0]
                for cnt in range(len(self.stack) - 1):
                    if self.stack[cnt] < self.min_num:
                        self.min_num = self.stack[cnt]
            del(self.stack[-1])
            print("pop", self.stack, self.min_num)
            return True

        elif len(self.stack) == 1:
            del(self.stack[0])
            self.min_num = None
            return True
        return False

    #方法一：维护一个最小数，插入和删除时进行判断
    #特点：适用于pop()时不容易命中最小数
    def min(self):
        return self.min_num

if __name__ == "__main__":
    M = MyStack()
    for num in [5, 4, 3, 2, 1, 3, 4]:
        M.push(num)
    M.pop()
    M.pop()
    print(M.min())