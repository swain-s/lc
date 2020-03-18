# 问题描述
# 模板：

class LeftRotateStr(object):
    def __init__(self):
        pass

    def left_totate_str(self, str, n):
        if n == 0 or str == None or len(str) == 0:
            return str

        new_str = ""
        for char in str[n:]:
            new_str += char
        for char in str[:n]:
            new_str += char

        return new_str


if __name__ == "__main__":
    S = LeftRotateStr()
    print(S.left_totate_str("abcdefg", 3))