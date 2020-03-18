# 问题描述
# 模板：

class FirstAppearOnce(object):
    def __init__(self):
        self.str = ""
        self.c_cnt = []


    def insert_a_char(self, char):
        self.str += char
        self.c_cnt.append(1)
        for pos in range(len(self.str)-1):
            if self.str[pos] == self.str[-1]:
                self.c_cnt[pos] += 1
                self.c_cnt[-1] += 1

    def first_appear_once(self):
        if len(self.str) <= 1:
            return self.str

        for pos in range(len(self.c_cnt)):
            if self.c_cnt[pos] == 1:
                return self.str[pos]

        return "#"

if __name__ == "__main__":
    S = FirstAppearOnce()
    str = "google"
    for s in str:
        S.insert_a_char(s)
        print(S.c_cnt)
        print(S.first_appear_once())
