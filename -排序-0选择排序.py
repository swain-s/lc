import random
a = [random.randint(0, 10) for i in range(10)]
print(a)

def select_sort(a):
    for minnum in range(0, len(a)):
            a[minnum] = min(a[minnum:len(a)])
    print("3-select_sort:    ", a)
select_sort(a)