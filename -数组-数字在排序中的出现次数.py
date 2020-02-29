# 问题描述
# 模板：

class TimesOfNum(object):
    def __init__(self):
        pass

    def time_of_num(self, arr, k):
        if len(arr) == 0 or arr == None:
            return 0
        
        def bin_search(tar, arr, le, ri):
            if len(arr) == 0:
                return False

            if ri - le <= 1:
                if arr[le] == tar or arr[ri] == tar:
                    return le
                elif arr[ri] != tar and arr[ri] != tar:
                    return -1

            mid = int(le + (ri - le)/2)
            if tar == arr[mid]:
                return mid
            elif tar > arr[mid]:
                return bin_search(tar, arr, mid, ri)
            elif tar < arr[mid]:
                return bin_search(tar, arr, le, mid)

        pos = bin_search(k, arr, 0, len(arr)-1)
        if pos == -1:
            return 0

        cnt = 1
        for p in range(pos-1, -1, -1):
            if arr[p] == k:
                cnt += 1
            else:
                break
        for p in range(pos+1, len(arr)):
            if arr[p] == k:
                cnt += 1
            else:
                break
        return cnt


if __name__ == "__main__":
    S = TimesOfNum()
    print(S.time_of_num([1, 3, 3, 5, 7, 9, 10], 1))