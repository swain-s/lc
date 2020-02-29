import random
a = [random.randint(0, 10) for i in range(10)]
print(a)

def merge_sort(array):
    def _merge_sort(a, l, r):
        if l >=r :
            return 0
        mid = int(l + (r - l) / 2)
        _merge_sort(a, l, mid)
        _merge_sort(a, mid+1, r)

        def merge(a, l, mid, r):
            new_a = []
            i = l
            j = mid+1
            while True:
                if i > mid:
                    break
                if j > r:
                    break
                if a[i] <= a[j]:
                    new_a.append(a[i])
                    i += 1
                elif a[i] > a[j]:
                    new_a.append(a[j])
                    j += 1
            for lrest in a[i:mid+1]:
                new_a.append(lrest)
            for rrest in a[j:r+1]:
                new_a.append(rrest)
            a[l:r+1] = new_a
            return merge

        merge(a, l, mid, r)
        return _merge_sort

    lena = len(array)-1
    _merge_sort(array, 0, lena)

#merge_sort(a)
#print(a)