# 问题描述:输入一个字符串,按字典序打印出该字符串中字符的所有排列。例如输入字符串abc,则打印出由字符a,b,c
# 输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母
#模板：abcdab

class Permutation(object):
    def __init__(self):
        pass

    #方法一：动态规划
    def permutation(self, string):
        pass


    #方法二：递归（结果正确，但是顺序不是字典序，不给通过）
    def permutation_(self, string):
        if string == None:
            return None
        elif len(string) == 0:
            return []
        s_arr = []
        for char in string:
            s_arr.append(char)

        def n_permutation(arr):
            #print("input:", arr, type(arr))
            if len(arr) == 1:
                return [[arr[0]]]

            result = []
            for pos in range(len(arr)):
                new_arr = [ele for ele in arr]
                new_arr.pop(pos)
                char = arr[pos]
                res = n_permutation(new_arr)
                for re_arr in res:
                    re_arr.insert(0, char)
                    result.append(re_arr)
            return result
        all =  n_permutation(s_arr)
        str = []
        for arr in all:
            s = ""
            for char in arr:
                s += char
            str.append(s)
        print(str)
        return self.my_set(str)

    #辅助一
    def my_set(self, li):
        set_li = []
        for ele in li:
            signal = 1
            for s_ele in set_li:
                if s_ele == ele:
                    signal = 0
            if signal == 1:
                set_li.append(ele)
        return set_li


    # 附加：求出字符串的有多少种组合方式
    def how_many_ways(self, string):
        if string == None:
            return None
        if len(string) == 0:
            return 0

        s_dict = {}
        for char in string:
            sinal = 1
            for key in s_dict:
                if char == key:
                    s_dict[char] += 1
                    sinal = 0
            if sinal == 1:
                s_dict[char] = 1

        all_situ = 1
        for cnt in range(1, len(string)+1):
            all_situ *= cnt
        for key in s_dict:
            if s_dict[key] == 1:
                pass
            elif s_dict[key] > 1:
                same_situ = 1
                for cnt in range(1, s_dict[key]+1):
                    same_situ *= cnt
                all_situ -= (same_situ -1)

        return all_situ

    def test(self):
        arr = [1, 2, 3]
        print(arr.pop(2))

if __name__ == "__main__":
    S = Permutation()
    print(S.permutation_("abca"))