
class node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Meger_K(object):
    def __init__(self):
        self.all = []

    # step1: 建堆(小顶堆)
    def list_to_heap(self, arr):
        if arr == None or len(arr) == 0:
            return []

        for cnt in range(len(arr)):
            if cnt == 0:
                pass

            n_parent = int((cnt - 1) / 2)
            def swap(arr, i, j):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

            while cnt >= 1:
                if arr[n_parent].val > arr[cnt].val:
                    swap(arr, cnt, n_parent)
                cnt = n_parent
                n_parent = int((cnt - 1) / 2)

    # step2: 堆顶出堆
    def meger_k(self, arr):
        for x in arr:
            print(x.val, end=", ")
        print("")

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

            min = arr.pop(0)
            self.all.append(min)
            if min.next == None:
                if len(arr) >= 2 and arr[0].val > arr[1].val:
                    temp = arr[0]
                    arr[0] = arr[1]
                    arr[1] = temp
            else:
                arr.insert(0, min.next)

            self.meger_k(arr)

if __name__ == "__main__":
    l1 = [node(3), node(4), node(18), node(37), node(100)]
    l2 = [node(10), node(11), node(55), node(88)]
    l3 = [node(2), node(11), node(19), node(222), node(555)]
    arr = [l1, l2, l3]
    for l in arr:
        for pos in range(len(l)-1):
            l[pos].next = l[pos+1]

    list = []
    for l in arr:
        list.append(l[0])

    m = Meger_K()
    m.meger_k(list)

    all = m.all
    for node in all:
        print(node.val)