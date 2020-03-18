# 问题描述
# 模板：

class  SumOfTwoNum(object):
    def __init__(self):
        pass

    # 二分查找，返回位置
    def bin_search_(self, tar, arr, le, ri):
        if len(arr) == 0:
            return []

        if ri - le <= 1:
            if arr[le] == tar:
                return [le]
            elif arr[ri] == tar:
                return [ri]
            elif arr[le] < tar and arr[ri] > tar :
                return [le, ri]
            else:
                return []


        mid = int(le + (ri - le)/2)
        if tar == arr[mid]:
            return [mid]
        elif tar > arr[mid]:
            return self.bin_search_(tar, arr, mid, ri)
        elif tar < arr[mid]:
            return self.bin_search_(tar, arr, le, mid)

    #思路，二分法查找找到【最小 - s】的区间
    #从区间最小值开始遍历 + 二分查找
    def sum_of_two_num(self, arr, s):
        if arr == None or s == None or s == 0 or len(arr) <= 1 or arr[0] >= s:
            return []

        re = self.bin_search_(s, arr, 0, len(arr) - 1)
        #print(re)
        if re == []:
            re.append(len(arr))
        for pos in range(0, re[0]):
            remain = s - arr[pos]
            num = self.bin_search_(remain, arr, 0, re[0])
            #print("pos, num:", pos, num, arr[pos], arr[num[0]])
            if len(num) == 1:
                return [arr[pos], arr[num[0]]]
        return []

if __name__ == "__main__":
    S = SumOfTwoNum()
    #arr = [i for i in range(1, 12)]
    arr = [1,2,4,7,11,16]
    print(arr)
    print(S.sum_of_two_num(arr, 1))