# 问题描述：输入n个整数，找出其中最小的K个数
# 模板：

class LeastKNumbers(object):
    def __init__(self):
        pass

    #方法一：排序
        #分析：数据量较大时
    #方法二：
        #维护K个数的排序（数组、二叉树）
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

    def heap_pop_root(self, arr, last, k):
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
        heap_find_new_root(arr, 0, k)   #新的heap从0到root前，新heap重新排序

    def least_k_numbers(self, arr, k):
        if k == 0 or len(arr) < 1 or k > len(arr):
            return []

        for i in range(k):
            self.add_a_to_heap_from_bottle(arr, i)

        for pos in range(k, len(arr)):
            if arr[pos] < arr[0]:
                def swap(arr, i, j):
                    temp = arr[i]
                    arr[i] = arr[j]
                    arr[j] = temp
                swap(arr, 0, pos)
                def heap_find_new_root(arr, l, r):
                    # arr[l:r+1]is a heap
                    root = l
                    left = 2 * root + 1
                    right = 2 * root + 2
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
                heap_find_new_root(arr, 0, k-1)

        return arr[:k]




if __name__ == "__main__":
    S = LeastKNumbers()

    arr = [1,   10, 5,   6, 2, 7, 4,    9, 3, 8, 11]
    print(S.least_k_numbers(arr, 7))