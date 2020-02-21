# -*- coding:utf-8 -*-
#在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
class Solution():
    # array 二维列表
    def bin_search(self, tar, arr, le, ri):
        if len(arr) == 0:
            return False

        if ri - le <= 1:
            if arr[le] == tar or arr[ri] == tar:
                return True
            elif arr[ri] != tar and arr[ri] != tar:
                return False

        mid = int(le + (ri - le)/2)
        if tar == arr[mid]:
            return True
        elif tar > arr[mid]:
            return self.bin_search(tar, arr, mid, ri)
        elif tar < arr[mid]:
            return self.bin_search(tar, arr, le, mid)

    def Find(self, target, array):
        # write code here
        for arr in array:
            if self.bin_search(target, arr, 0, len(arr)-1):
                return True
        return False

B = Solution()
#a = B.bin_search(5, [1, 3, 5, 7, 9], 0, 4)
#print(a)
b = B.Find(1,[[]])
print(b)