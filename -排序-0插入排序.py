import random
a = [random.randint(0, 10) for i in range(10)]
print(a)

def insert_sort(a):
    for me in range(1, len(a)):
        for prev in range(0, me):
            if a[me] < a[prev]:
                temp = a[me]
                del(a[me])
                a.insert(prev-1, temp)
    print("2-insert_sort:    ", a)
insert_sort(a)