pause = [0]
class Bin_search():
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

B = Bin_search()
B.bin_search(3, [1, 3, 5, 7, 9], 0, 4)
