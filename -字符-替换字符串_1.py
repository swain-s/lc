# -*- coding:utf-8 -*-
#请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        new_s = []
        for cursor in range(len(s)):
            if s[cursor] == " ":
                new_s.append("%20")
            else:
                new_s.append(s[cursor])
        return "".join(new_s)

S = Solution()
b = S.replaceSpace("hello world")
print(b)