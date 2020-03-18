# 问题描述
# 模板：

class IsContinuous(object):
    def __init__(self):
        pass

    def is_continuous(self, arr):
        if len(arr) != 5:
            return False

        new_arr = []
        zero_cnt = 0
        for pos in range(len(arr)):
            if arr[pos] == 0:
                zero_cnt += 1
            elif arr[pos] > 0:
                insert_pos = 0
                for num in new_arr:
                    if num == arr[pos]:
                        return False
                    elif num < arr[pos]:
                        insert_pos += 1
                new_arr.insert(insert_pos, arr[pos])

        print(new_arr[-1], new_arr[0], zero_cnt)
        if len(new_arr) == 1:
            return True
        else:
            if new_arr[-1] - new_arr[0] <= 4:
                return True
            else:
                return False


if __name__ == "__main__":
    S = IsContinuous()
    print(S.is_continuous([2, 3, 6, 7, 0]))