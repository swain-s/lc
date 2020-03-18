# 问题描述
# 模板：

class Str_To_Int(object):
    def __init__(self):
        pass

    def str_to_int(self, str):

        num = 0
        cnt = 1
        for pos in range(len(str)-1, -1, -1):
            if pos == 0:
                if ord(str[pos]) == 43:
                    return +num
                elif ord(str[pos]) == 45:
                    return -num
            if ord(str[pos]) in range(48, 57):
                num += cnt * (ord(str[pos]) - 48)
                cnt *= 10
            else:
                return 0
        return num


if __name__ == "__main__":
    S = Str_To_Int()
    print(ord("a"), ord("z"), ord("A"), ord("Z"), ord("+"), ord("-"), ord("0"), ord("9"))
    print(S.str_to_int("+12345"))