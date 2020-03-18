def solution(arr):
    if len(arr) <= 1:
        return 0

    for head in range(len(arr)):
        for tail in range(len(arr)-1, -1, -1):
            if tail -1 == head and arr[head] == arr[tail]:
                return 4
            if tail <= head:
                return 0

solution([1,4,2,2,3,3,2,4,1])

