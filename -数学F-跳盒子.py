
def solution(step_list):

    def jump(arr, cnt):
        if len(arr) == 0:
            return cnt
        re = []
        for step in range(arr[0], 0, -1):
            if step >= len(arr) - 1:
                return cnt + 1
            else:
                re.append(jump(arr[step:], cnt+1))
        if len(re) == 0:
            return cnt + 100
        return cnt + min(re)

    return jump(step_list, 0)

print(solution([0]))
