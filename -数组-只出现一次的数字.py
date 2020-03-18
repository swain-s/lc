# 问题描述
# 模板：

class TwoNumAppearOnce(object):
    def __init__(self):
        pass

    def two_num_appear_once(self, arr):
        xor_sum = 0
        for num in arr:
            xor_sum ^= num

        pos_1 = 0
        while xor_sum != 1:
            xor_sum = xor_sum >> 1
            pos_1 += 1

        zero_xor_sum = 0
        one_xor_sum = 0
        for num in arr:
            #print((num & 0xffffffff) >> pos_1 << (32 - pos_1 - 1))
            if ((num & 0xffffffff) >> pos_1) & 1  == 0:
                print("0:", num)
                zero_xor_sum ^= num
            else:
                print("1:", num)
                one_xor_sum ^= num

        return [zero_xor_sum, one_xor_sum]

if __name__ == "__main__":
    S = TwoNumAppearOnce()
    print(S.two_num_appear_once([2,4,3,6,3,2,5,5]))
    print((8 & 0xffffffff) >> 3)