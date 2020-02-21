# 问题描述：栈的压入弹出顺序
# 模板：压入 = 【1， 2， 3， 4， 5】， 是否存在【4， 5， 3， 2， 1】为弹出顺序

class PopOrder(object):
    def __init__(self):
        pass

    def pop_order(self, push_arr, pop_arr):
        stack = []
        pop_cnt = 0
        for num in push_arr:
            stack.append(num)
            print(stack, pop_arr[pop_cnt])
            while stack and stack[-1] == pop_arr[pop_cnt]:
                stack.pop()
                pop_cnt += 1

        if len(stack) == 0:
            return True
        return False


if __name__ == "__main__":
    S = PopOrder()
    print(S.pop_order([1 , 2, 3, 4, 5], [4, 2, 3, 5,1]))