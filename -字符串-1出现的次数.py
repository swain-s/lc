# 问题描述
# 模板：

class TimesOf1(object):
    def __init__(self):
        pass

    def times_of_1(self, n):
        clist = ["%d" % cnt for cnt in range(n+1)]
        print(clist)
        cnt = 0

        chr_n = "%d" % n
        for ch_cnt in range(len(chr_n)-1, -1, -1):
            for cnum in clist:
                if ch_cnt < len(cnum) and cnum[ch_cnt] == "1":
                    cnt += 1
        return cnt

if __name__ == "__main__":
    T = TimesOf1()
    print(T.times_of_1(10))