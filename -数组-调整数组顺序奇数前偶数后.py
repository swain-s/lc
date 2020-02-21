# 问题描述：调整数组元素，奇数前，偶数后
# 模板：

class ReorderArr(object):
    def __init__(self):
        self.r_arr = [1, 2, 3, 4, 5, 6, 7]

    #方法一：数组进行插入删除操作（pass）
    def reorder_arr(self, arr):
        del_cnt = 0
        for cnt in range(len(arr)):
            if arr[cnt-del_cnt] % 2 == 0:
                arr.append(arr[cnt-del_cnt])
                del(arr[cnt-del_cnt])
                del_cnt += 1
        return arr

    #方法二：新建数组，合并
    #分析：一：遍历一遍，新建两个数组， 二：遍历两遍，新建一个数组
    def reorder_arr_(self, arr):
        odd_arr = []
        even_arr = []
        for num in arr:
            if num % 2 == 1:
                odd_arr.append(num)
            elif num % 2 == 0:
                even_arr.append(num)

        while(arr):
            arr.pop()
        for num in odd_arr:
            arr.append(num)
        for num in even_arr:
            arr.append(num)
        return arr

    def main(self):
        self.reorder_arr_(self.r_arr)
        print(self.r_arr)

if __name__ == "__main__":
    S = ReorderArr()
    print(S.reorder_arr([1, 2, 3, 4, 5, 6, 7]))
    print(S.reorder_arr_([1, 2, 3, 4, 5, 6, 7]))
    S.main()