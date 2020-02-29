# 问题描述
# 模板：

class ArraryToMinNum(object):
    def __init__(self):
        pass

    #方法一：基数排序
    #分析：未通过 【3334,3,3333332】
    def arr_to_min_num(self, arr):
        if arr == None or len(arr) == 0:
            return ""

        clist = []
        max_num = arr[0]
        for num in arr:
            clist.append("%d" % num)
            if num > max_num:
                max_num = num

        chr_n = "%d" % max_num

        old_bucket = [[] for cnt in range(10)]
        old_bucket[0] = clist
        for ch_cnt in range(len(chr_n)-1, -1, -1):
            new_bucket = [[] for cnt in range(10)]
            for cnum_list in old_bucket:
                for cnum in cnum_list:
                    if ch_cnt >= len(cnum):
                        new_bucket[int(cnum[-1])].append(cnum)  #重点 34 -(补为)->  34444
                    else:
                        new_bucket[int(cnum[ch_cnt])].append(cnum)
            old_bucket = new_bucket

        chr_max = ""
        for cnum_list in old_bucket:
            for cnum in cnum_list:
                chr_max += cnum
        return int(chr_max)

if __name__ == "__main__":
    S = ArraryToMinNum()
    print(S.arr_to_min_num([3334, 3, 3333332]))