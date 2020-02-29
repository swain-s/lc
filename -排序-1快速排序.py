import random
a = [random.randint(0, 10) for i in range(10)]
print(a)

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[int(len(arr) / 2)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)
#a = quicksort(a)
#print(a)

def quick_sort(a, l, r):
    if l >= r:
        return
    #输入：无序数组
    #   随意选取一个数target：左右指针移动，比target小的在左边，比target大的在右边
    #   如 【6， 3， 7， 1， 4， 5】 选择6，则：
    #   输出【3， 1， 4， 5，   6，     7】
    def partition(a, l, r):
        target = a[l]
        # l可以被覆盖了
        # 右边可以动，左边卡主，但左边可以被覆盖
        while l < r:
            while l < r and a[r] >= target:
                r -= 1
            # 右边卡主，交换后，左边可以动，右边可以被覆盖
            a[l] = a[r]
            while l < r and a[l] < target:
                l += 1
            a[r] = a[l]
        a[l] = target
        return l
        #此时的l为6的位置了

    t = partition(a, l, r)
    quick_sort(a, l, t-1)
    # 对右边部分执行快速排序
    quick_sort(a, t+1, r)
quick_sort(a, 0, len(a)-1)
print(a)