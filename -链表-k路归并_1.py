
class node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Meger_K(object):
    def __init__(self):
        self.all = []

    # step1: _建堆：第n个数入堆
    def add_to_heap(self, arr, n):
        if n < 1:
            return
        n_parent = int((n-1)/2)
        def swap(arr, i, j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        while n >= 1:
            if arr[n_parent].val > arr[n].val:
                swap(arr, n, n_parent)
            n = n_parent
            n_parent = int((n-1)/2)

    # step2: 建堆(小顶堆)
    def list_to_heap(self, arr):
        if arr == None or len(arr) == 0:
            return None
        else:
            for cnt in range(len(arr)):
                self.add_to_heap(arr, cnt)
            return arr

    # step3: 堆顶指针后移
    def meger_k(self, arr):
        if len(arr) == 0:
            return
        elif len(arr) == 1:
            temp = arr[0]
            while temp != None:
                self.all.append(temp)
                temp = temp.next
            return
        elif len(arr) > 1:
            self.list_to_heap(arr)
            self.all.append(arr[0])
            min = arr.pop(0)
            if min.next != None:
                arr.insert(min.next)
            self.meger_k(arr)


if __name__ == "__main__":
    l1 = [node(1), node(4), node(18), node(37), node(100)]
    l2 = [node(10), node(11), node(55), node(88)]
    l3 = [node(5), node(11), node(19), node(222), node(555)]
    arr = [l1[0], l2[0], l3[0]]
    for l in [l1, l2 ,l3]:
        for pos in range(len(l) - 1):
            l[pos].next = l[pos + 1]

    m = Meger_K()
    m.meger_k(arr)