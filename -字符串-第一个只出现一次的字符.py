# 问题描述
# 模板：

class FirstUniqueChar(object):
    def __init__(self):
        pass

    def first_unique_cahr(self, str):
        if len(str) == 0 or str == None:
            return -1

        #大写的在前，小写的在后
        hash_table = [0] * 52
        chr_arr = []
        order_arr = []
        for pos in range(len(str)):
            asc = ord(str[pos])
            if asc <= 90:
                if hash_table[asc - 65] == 0:
                    hash_table[asc - 65] += 1
                    order_arr.append(pos)
                    chr_arr.append(str[pos])
                else:
                    hash_table[asc - 65] += 1
            elif asc >= 97: #to 122
                if hash_table[asc - 97 + 26] == 0:
                    hash_table[asc - 97 + 26] += 1
                    order_arr.append(pos)
                    chr_arr.append(str[pos])
                else:
                    hash_table[asc - 97 + 26] += 1

        for pos in range(len(order_arr)):
            asc = ord(chr_arr[pos])
            if asc <= 90:
                if hash_table[asc - 65] == 1:
                    return order_arr[pos]
            else:
                if hash_table[asc - 97 + 26] == 1:
                    return order_arr[pos]
        return -1


if __name__ == "__main__":
    F = FirstUniqueChar()
    print(F.first_unique_cahr("azjfahgkjafaifjkd"))