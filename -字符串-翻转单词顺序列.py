# 问题描述
# 模板：

class ReverseWords(object):
    def __init__(self):
        pass

    def reverse_words(self, str):
        if str == "":
            return ""

        new_str = []
        start = len(str) - 1
        for cnt in range(len(str) - 1, -1, -1):
            if cnt == 0:
                new_str.append(str[cnt:start + 1])
                re_str = ""
                for char in new_str:
                    re_str += char
                return re_str

            if str[cnt] == " ":
                new_str.append(str[cnt + 1:start + 1])
                new_str.append(" ")
                start = cnt - 1

if __name__ == "__main__":
    S = ReverseWords()
    print(S.reverse_words("student. a am I"))
    print(S.reverse_words("wonderful"))