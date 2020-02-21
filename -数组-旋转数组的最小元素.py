# 问题描述：旋转的有序数组（只循环一次）
# 模板：【3， 4， 5， 1， 2】
# 思路：找到旋转点：二分查找

class MinOfRotatearr(object):
    def __init__(self):
        pass

    #方法一：暴力破解
    def min_of_rotatearr(self, rotatearr):
        if len(rotatearr) == 0:
            return 0

        minnum = rotatearr[0]
        for num in rotatearr:
            if num < minnum:
                minnum = num

        return minnum

    #方法二：二分查找旋转点
    #时间复杂度：log(n)
    def min_of_rotatearr_(self, rotatearr):
        if len(rotatearr) == 0:
            return 0

        def bin_search(arr, le, ri):
            if ri == le + 1 and arr[ri] <= arr[le]:
                return arr[ri]

            mid = int(le + (ri - le)/2)
            if arr[mid] > arr[le]:
                return bin_search(arr, mid, ri)
            if arr[mid] < arr[le]:
                return bin_search(arr, le, mid)

        min_num = bin_search(rotatearr, 0, len(rotatearr)-1)
        return min_num


if __name__ == "__main__":
    S = MinOfRotatearr()
    print(S.min_of_rotatearr([3, 4, 5, 6, 0, 2]))
    print(S.min_of_rotatearr_([3, 4, 5, 6, 0, 2]))