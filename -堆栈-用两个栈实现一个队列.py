# 问题描述:用两个栈实现一个队列
# 模板：fstack = [], sstack = []

class TwoStackEueqlOneQueue(object):
    def __init__(self):
        self.fstack = []
        self.sstack = []

    def push(self, node):
        self.fstack.append(node)

    def pop(self):
        while self.fstack:
            self.sstack.append(self.fstack.pop())
        self.sstack.pop()
        while self.sstack:
            self.fstack.append(self.sstack.pop())
        return self.fstack

if __name__ == "__main__":
    S = TwoStackEueqlOneQueue()

    S.push(3)
    S.push(5)
    S.push(7)
    S.push(9)
    S.push(6)
    print(S.fstack)
    print(S.pop())
    print(S.pop())