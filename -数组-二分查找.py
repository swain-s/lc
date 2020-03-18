pause = [0]
class Bin_search():
    # 二分查找返回 True or False
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

B = Bin_search()
print(B.bin_search(4, [1, 3, 5, 7, 9], 0, 4))
print(B.bin_search_(1, [1, 3, 5, 7, 9], 0, 4))
