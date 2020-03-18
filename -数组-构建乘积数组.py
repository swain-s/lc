# 问题描述
# 模板：

class Mul_Arr(object):
    def __init__(self):
        pass

    def mul_arr(self, arr_a):
        if arr_a == None or len(arr_a) == 0:
            return []

        arr_b = [1] * len(arr_a)
        for posa in range(len(arr_a)):
            for posb in range(len(arr_b)):
                if posb != posa:
                    arr_b[posb] *= arr_a[posa]
        return arr_b


if __name__ == "__main__":
    S = Mul_Arr()
    print(S.mul_arr([1, 2, 3, 4, 5]))