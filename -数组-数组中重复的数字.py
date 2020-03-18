# 问题描述
# 模板：

class Duplicate(object):
    def __init__(self):
        pass

    def duplicate(self, arr, dup):
        hash_table = [0] * len(arr)
        for num in arr:
            hash_table[num] += 1
        print(hash_table)
        for pos in range(len(arr)):
            if hash_table[pos] > 1:
                dup[0] = pos
                return True
        return False

if __name__ == "__main__":
    S = Duplicate()
    print(S.duplicate([2,3,1,0,2,5,3], [-1]))