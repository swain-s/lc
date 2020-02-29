import random
a = [random.randint(0, 10) for i in range(10)]
print(a)

def bubble_sort(a):
    for j in range(0, len(a)):
        last = (len(a)-1) - j
        for i in range(0, last):
            if a[i] > a[i+1]:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
    print("1-bubble_sort:    ", a)
bubble_sort(a)