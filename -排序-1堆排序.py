#堆排序(原地排序)
# [1,   10, 5,   6, 2, 7, 4,    9, 3, 8, 11]

class HeapSort():
    def __init__(self):
        pass
    #heap_node:
    #   last = int((n-1)/2)
    #   left = 2n + 1
    #   right = 2n + 2
    def add_a_to_heap_from_bottle(self, arr, new):
        #arr[0:last+1]是堆，arr[new] 在arr[last]后一个
        if new < 1:
            return

        n_parent = int((new-1)/2)
        def swap(arr, i, j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

        while new >= 1:
            if arr[n_parent] < arr[new]:
                swap(arr, new, n_parent)
            new = n_parent
            n_parent = int((new-1)/2)

    def all_to_heap(self, arr):
        if arr == None or len(arr) == 0:
            return []

        for cnt in range(len(arr)):
            self.add_a_to_heap_from_bottle(arr, cnt)
        return arr

    def heap_pop_root(self, arr, last):
        if last <= 0:
            return
        def swap(arr, i, j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        #把heap中最后一个放到顶部，   root放到原来最小的位置，heap.pop(root)
        def heap_find_new_root(arr, l, r):
            #arr[l:r+1]is a heap
            root = l
            left = 2*root +1
            right = 2*root +2
            max = root
            if left <= r:
                if arr[max] < arr[left]:
                    max = left
            if right <= r:
                if arr[max] < arr[right]:
                    max = right
            if max != root:
                swap(arr, root, max)

            if left <= r:
                heap_find_new_root(arr, left, r)
            if right <= r:
                heap_find_new_root(arr, right, r)

        swap(arr, 0, last)   #交换root到最后
        heap_find_new_root(arr, 0, last-1)   #新的heap从0到root前，新heap重新排序

    def heap_pop_all(self, arr):
        last = len(arr) -1
        while last > 0:
            self.heap_pop_root(arr, last)
            last -= 1

    def heap_sort(self, arr):
        heap_arr = self.all_to_heap(arr)
        self.heap_pop_all(heap_arr)
        return heap_arr

if __name__ == "__main__":
    H = HeapSort()

    import random
    a = [random.randint(0, 10) for i in range(10)]
    print(a)

    print(H.heap_sort(a))