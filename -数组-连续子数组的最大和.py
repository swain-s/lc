# 问题描述：数组子序列的最大和
# 模板：【6，-3，-2，7，15，1，2，2】

class GreatestSubArr(object):
    def __init__(self):
        pass

    #方法一：暴力破解
    def greatest_subarr(self, arr):
        maxnum = arr[0]
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                sum = 0
                for num in arr[i:j+1]:
                    sum += num
                    if sum > maxnum:
                        maxnum = sum
        return maxnum

if __name__ == "__main__":
    S = GreatestSubArr()

    result = S.greatest_subarr([6, -3, -2, 7, -15, 1, 2, 2])
    print(result)