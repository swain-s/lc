# 问题描述
# 模板：

class InversePaires(object):
    def __init__(self):
        pass

    #方法一：冒泡查找
    def inverse_paires(self, arr):
        if arr == None and len(arr) <= 1:
            return 0

        cnt = 0
        for j in range(0, len(arr)):
            last = (len(arr) - 1) - j
            for i in range(0, last):
                if arr[i] > arr[i + 1]:
                    cnt += 1
                    temp = arr[i]
                    arr[i] = arr[i + 1]
                    arr[i + 1] = temp
        return cnt

    #

    def merge_count_2(list):
        if len(list) <= 1:
            return list, 0
        mid = len(list) // 2
        left_li, left_cont = merge_count(list[:mid])
        right_li, right_cont = merge_count(list[mid:])
        count = left_cont + right_cont

        result = []
        while 0 < len(left_li) and 0 < len(right_li):
            if left_li[0] > right_li[0]:
                result.append(left_li.pop(0))
                count += len(right_li)
            else:
                result.append(right_li.pop(0))
        result += left_li
        result += right_li
        return result, count

if __name__ == "__main__":
    S = InversePaires()
    print(S.inverse_paires([1,2,3,4,5,6,7,0]))