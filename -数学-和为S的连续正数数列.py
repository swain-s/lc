# 问题描述
# 模板：

class SeqOfSumS(object):
    def __init__(self):
        pass

    def seq_of_sum_s(self, s):
        def seq_of_sum_s(start, left, s):
            if left - start < 0:
                return []
            elif left - start == 0:
                return [start]
            else:
                if start >= s:
                    return []

                result = seq_of_sum_s(start+1, left-start, s)
                if len(result) > 0:
                    result.insert(0, start)
                    return result
                return []

        re_arr = []
        for i in range(1, s):
            re = seq_of_sum_s(i, s, s)
            if len(re) > 0:
                re_arr.append(re)

        return re_arr

if __name__ == "__main__":
    S = SeqOfSumS()
    print(S.seq_of_sum_s(7))