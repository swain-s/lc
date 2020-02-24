# 问题描述：请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法
# 模板：

class RectCover(object):
    def __init__(self):
        pass

    def rect_cover(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        elif n>= 3:
            sma = 1
            big = 2
            for n in range(3, n+1):
                sum = sma + big
                sma = big
                big = sum
            return big
        return None


if __name__ == "__main__":
    S = RectCover()
    print(S.rect_cover(6))