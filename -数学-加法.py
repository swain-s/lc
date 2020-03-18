# 问题描述
# 模板：

class Add(object):
    def __init__(self):
        pass

    def add(self, a, b):
        if a & b == 0:
            return a ^ b

        s_xor = a ^ b
        s_and = a & b
        return self.add(s_xor, s_and << 1)

    def add_sub(self, a, b):

        sum =  self.add(a, b)
        return sum if sum << 31 == 0 else ~ sum

if __name__ == "__main__":
    S = Add()
    print(S.add_sub(3, 4))

