# 问题描述：每次可以跳一级或两级，跳上n级的方法
# 模板：
# 思路：逆向思维
# 公式：f(n) = f(n-1) + f(n-2) : f(n)：到第n级台阶有多少种跳法

class JumpFloor(object):
    def __init__(self):
        pass

    #方法一：递归
    #时间复杂度：较大
    def jumpfloor(self, n):
        #num = 0
        if n == 0:
            num = 0
            return num
        if n == 1:
            num = 1
            return num
        if n == 2:
            num = 2
            return num
        if n > 2:
            num = self.jumpfloor(n-1) + self.jumpfloor(n-2)
            return num

        exit(-1)

    #方法二：迭代 + 赋值
    #时间复杂度：小
    def jumpfloor_(self, n):
        num = 0
        if n == 0:
            num = 0
        if n == 1:
            num = 1
        if n == 2:
            num = 2
        if n > 1:
            n_2 = 1
            n_1 = 2
            for cnt in range(3, n+1):
                num = n_1 + n_2
                n_2 = n_1
                n_1 = num
        else:
            exit(-1)
        return num

    #方法三：迭代 + 概率论
    def probability(self, n):
        num = 0
        if n == 0:
            num = 0
        if n == 1:
            num = 1
        if n == 2:
            num = 2
        if n > 2:
            num_two = 10
            pass

if __name__ == "__main__":
    J = JumpFloor()

    result = J.jumpfloor(7)
    print(result)

    result_ = J.jumpfloor_(7)
    print(result_)