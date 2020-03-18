# 问题描述
# 模板：

class Match(object):
    def __init__(self):
        pass

    def match(self, str, pattern):
        print(str, pattern)
        if str == None or pattern == None:
            return False

        elif len(str) == 0 and len(pattern) == 0:
            return True
        elif len(str) == 0 :
            signal = False
            double = 0
            for char in pattern:
                if double == 0:
                    double = 1
                elif double == 1:
                    if char == "*":
                        signal = True
                    else:
                        return False
            return signal
        elif len(pattern) == 0:
            return False
        else:
            if len(pattern) > 1:
                if len(pattern) > 1 and pattern[1] == "*":
                    if len(str) == 1 and pattern[-1] == str[0]:
                        return True
                    if pattern[0] == str[0] or pattern[0] == ".":
                        return self.match(str[1:], pattern)
                    else:
                        return self.match(str, pattern[2:])
                else:
                    if str[0] == pattern[0] or pattern[0] == ".":
                        return self.match(str[1:], pattern[1:])
                    else:
                        return False
            elif len(pattern) == 1:
                if pattern[0] == str[0] or pattern == ".":
                    return self.match(str[1:], pattern[1:])
                else:
                    return False

    #题目没说清楚 " '*' 前面的"的是指：a)前面的一个字符， b）前面的一串字符
    def match_(self, str, pattern):
        if str == None or pattern == None:
            return False
        elif len(str) == 0 and len(pattern) == 0:
            return True
        elif len(str) == 0:
            if pattern[-1] == "*":
                return True
            else:
                return False
        elif len(pattern) == 0:
            return False

        signal = 0
        for pos in range(len(pattern)):
            if pattern[pos] == "*":
                if signal == 1:
                    return self.match_(str[1:], pattern[pos+1:])
            elif pattern[pos] == str[0] or pattern[pos] == ".":
                signal = 1
        if str[0] == pattern[0] or pattern[0] == ".":
            return self.match_(str[1:], pattern[1:])
        return False


if __name__ == "__main__":
    S = Match()
    #print(S.match("aaa", "a.a"))
    print(S.match("aaa", "a*a"))
    #print(S.match("aaa", "ab*ac*a"))
    #print(S.match("aaa", "ab*a"))
    #print(S.match("aaa", "aa.a"))