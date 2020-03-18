# 问题描述
# 模板：

class IsNumeric(object):
    def __init__(self):
        pass

    def is_numeric(self, str):
        has_point = False

        not_point = True # e之后的小数点
        e_front = False
        e = False
        e_behind = False

        for pos in range(len(str)):
            if str[pos] == "+" or str[pos] == "-":
                if pos == 0 or str[pos-1] == "e" or str[pos-1] == "E":
                    pass
                else:
                    print("1", end="")
                    return False
            elif str[pos] == ".":
                if has_point == True:
                    return False
                else:
                    has_point = True

                if not_point == False:
                    print("2", end="")
                    return False
                else:
                    not_point = False
            elif ord(str[pos]) in range(48, 57+1):
                if e_front == False:
                    e_front = True
                if e == True and e_behind == False:
                    e_behind = True
            elif str[pos] == "e" or "E":
                if e == False:
                    e = True
                else:
                    print("3", end="")
                    return False
            else:
                print("4", end="")
                return False

        if e == True:
            if e_front & e_behind & not_point == 1:
                return True
            else:
                print("5", end="")
                return False
        return True


if __name__ == "__main__":
    S = IsNumeric()
    arr = ["+100", "5e2", "-123", "3.1416", "-1E-16",          "12e", "1a3.14", "1.2.3", "+-5", "12e+4.3"]
    for str in arr:
        print(S.is_numeric(str))