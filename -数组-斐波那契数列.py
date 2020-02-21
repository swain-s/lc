#菲波那切数列：打印第n项
#模型：0 1 1 2 3 5 8 13...
class Fibonacci(object):
    def __init__(self):
        self.arr = []

    #方法一：递归
    #时间复杂度：较大，每个值重复计算很多次
    def fibonacci(self, n):
        #num = 0
        if n == 0:
            num = 0
            return num
        if n == 1:
            num = 1
            return num
        if n > 1:
            num = self.fibonacci(n-1) + self.fibonacci(n-2)
            return num
        exit(-1)

    #方法二：迭代
    #时间复杂度：小
    def fibonacci_(self, n):
        num = 0
        if n == 0:
            num = 0
        if n == 1:
            num = 1
        if n > 1:
            n_2 = 0
            n_1 = 1
            for cnt in range(2, n+1):
                num = n_1 + n_2
                n_2 = n_1
                n_1 = num
        else:
            exit(-1)
        return num


if __name__ == "__main__":
    F = Fibonacci()

    result = F.fibonacci(8)
    print(result)

    result_ = F.fibonacci_(8)
    print(result_)