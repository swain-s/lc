# 问题描述
# 模板：

class UglyNum(object):
    def __init__(self):
        pass

    def ugly_num(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        arr = [1]
        cnt_arr = [0]

        cur = 0
        farr = [2, 3, 5]
        for i in range(1, n):
            minnum = [arr[-1]*3, 0]
            for pos in range(cur, i):
                if arr[pos] * farr[cnt_arr[pos]] <= arr[-1]:
                    if cnt_arr[pos] == 2:
                        cnt_arr[pos] += 1
                        cur += 1
                    elif cnt_arr[pos] == 1 or cnt_arr[pos] == 0:
                        cnt_arr[pos] += 1
                elif arr[pos] * farr[cnt_arr[pos]] < minnum[0]:
                    minnum[0] = arr[pos] * farr[cnt_arr[pos]]
                    minnum[1] = pos

            arr.append(minnum[0])
            cnt_arr.append(0)
            if cnt_arr[minnum[1]] == 2:
                cnt_arr[minnum[1]] += 1
                cur += 1
            elif cnt_arr[minnum[1]] == 1 or cnt_arr[minnum[1]] == 0:
                cnt_arr[minnum[1]] += 1
            else:
                cnt_arr.append(0)
            print(arr)
            print(cnt_arr)
        return arr[-1]



if __name__ == "__main__":
    U = UglyNum()
    print(U.ugly_num(8))