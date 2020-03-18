# 问题描述
# 模板：

class Solution(object):
    def __init__(self):
        pass

    def solution(self, n):
        if n == 0:
            print("")
            return 0

        def points(cnt):
            if cnt == 1:
                hash_key = []
                hash_val = []
                return [[0, 1, 2, 3], [1, 1, 2, 2]]
            posi_key = []
            pos_val = []
            for num in [0, 1, 2, 2, 3, 3]:
                hash_key, hash_val = points(cnt -1)[0], points(cnt -1)[1]
                for key in hash_key:
                    key += num
                posi_key.append(hash_key)
                pos_val.append(hash_val)
            return posi
        posi = points(n)

        hash_key = []
        hash_val = []
        for arr in posi:
            sum = 0
            for num in arr:
                sum += num
            flag = 0
            for pos in range(len(hash_key)):
                if hash_key[pos] == sum:
                    flag = 1
                    hash_val[pos] += 1
            if flag == 0:
                hash_key.append(sum)
                hash_val.append(1)

        for pos in range(len(hash_key)):
            print("%d:%d" % (hash_key[pos], hash_val[pos]))

if __name__ == "__main__":
    S = Solution()

    n = int(input())
    S.solution(n)

