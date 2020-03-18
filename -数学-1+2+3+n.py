# 问题描述
# 模板：

class Sum(object):
    def __init__(self):
        self.sum = 0

    def sum_of_n(self, n):
        def new_sum(n):
            self.sum += n
            return n > 0 and new_sum(n-1)

        new_sum(n)
        return self.sum

if __name__ == "__main__":
    S = Sum()
    print(S.sum_of_n(4))