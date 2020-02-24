# 问题描述:数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 模板：[1, 2 ,3 ,1 ,4, 1, 1, 1, 5]

class MoreThanHalf(object):
    def __init__(self):
        pass

    #方法一：排序，返回中间数字
        #分析：数据量较大时比较复杂
    #方法二：hashmap
        #分析：数据较分散时，hash表比较长
    #方法三：删除不等数字（前后消除法）
        #数组的删除操作代价太高
    #方法四：存储当前出现的最大次数（出现次数消除法）
        #

    #方法二
    def hmore_than_half(self, arr):
        hash_map_v = [0 for i in range(100)]

        def hash_func(num):
            key = num
            return key

        max_t = 0
        max_num = 0

        for num in arr:
            k = hash_func(num)
            hash_map_v[k] += 1

            if hash_map_v[k] > max_t:
                max_num = num
                max_t = hash_map_v[k]

        if max_t > len(arr)/2:
            return max_num
        return 0



    #方法四
    def more_than_half(self, arr):
        if arr == None or len(arr) == 0:
            return None
        elif len(arr) == 1:
            return arr[0]
        na = arr[0]
        old = na   #避免偶然情况 1,2,3,2,4,2,5,2,6
        ta = 1
        for num in arr[1:]:
            print(na, ta, "--->", num)
            if num == na:
                ta += 1
            else:
                if ta == 1:
                    old = na
                    na = num
                elif ta > 0:
                    ta -= 1
        if ta > 0:
            if ta == 1 and na != old:
                return 0
            return na
        else:
            return 0

if __name__ == "__main__":
    S = MoreThanHalf()
    print(S.hmore_than_half([1,2,3,2,4,2,5,2,3,2]))