# 问题描述
# 模板：

class FirstAppearOnce(object):
    def __init__(self):
        self.str = ""
        self.hash_table = [0] * 52

    def insert_a_char(self, char):
        self.str += char
        def hash_func(char):
            if ord(char) in range(97, 122+1):
                return ord(char) - 97 + 26
            elif ord(char) in range(65, 90):
                return ord(char) - 65
        self.hash_table[hash_func(char)] += 1

    def first_appear_once(self):
        for h_cnt in range(len(self.hash_table)):
            if self.hash_table[h_cnt] == 1:
                if h_cnt <= 25:
                    return chr(65 + h_cnt)
                else:
                    return chr(97 + h_cnt)

if __name__ == "__main__":
    S = FirstAppearOnce()
    S.insert_a_char("a")
    S.insert_a_char("B")
    S.insert_a_char("c")
    print(S.first_appear_once())