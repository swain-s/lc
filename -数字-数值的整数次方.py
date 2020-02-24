# 问题描述：给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
#
# 保证base和exponent不同时为0
# 模板：

class Power(object):
    def __init__(self):
        pass

    def power(self, base, n):
        if n == 0:
            return 1
        fbase = float(base)
        mul = 1

        if n > 0:
            for cnt in range(n):
                mul = mul * fbase
            return mul
        if n < 0:
            for cnt in range(-n):
                mul = mul * fbase
            return float(1/mul)





if __name__ == "__main__":
    S = Power()
    print(S.power(2, -3))