W = 1
P = 2
import copy
class DP(object):
    def __init__(self):
        pass

    # 递减：错误
    def dp(self, wei, th, price):
        all_price = []

        flag = 0
        for T in range(len(th)):
            if th[T][W] < wei:
                flag = 1
                new_th = copy.deepcopy(th)
                new_th.pop(T)
                self.dp(wei - th[T][W], new_th, price + th[T][P])
                all_price.append(price + th[T][P])

        print(wei, price, all_price)
        if flag == 1:
            return max(all_price)
        else:
            return price

    # 递增：
    def dp_(self, wei, th, price):
        all_price = []

        flag = 0
        for T in range(len(th)):
            if th[T][W] + wei <= 8:
                flag += 1
                new_th = copy.deepcopy(th)
                new_th.pop(T)
                p = self.dp_(wei + th[T][W], new_th, price + th[T][P])
                all_price.append(p)

        if flag > 0:
            return max(all_price)
        else:
            return price

    def dp2(self, wei, th):
        dp = [[0] * (wei + 1) for cnt in range(len(th) + 1)]

        for w in range(1, wei + 1):
            for t in range(len(th)):
                if th[t][W] <= w:

                    before_max = dp[0][w - th[t][W]]
                    for cnt in range(t+1):
                        if before_max < dp[cnt][w - th[t][W]]:
                            before_max = dp[cnt][w - th[t][W]]
                    dp[t+1][w] = before_max + th[t][P]

        for p in dp:
            print(p)

if __name__ == "__main__":
    th = [[0, 2, 3],
          [1, 3, 4],
          [2, 4, 5],
          [3, 5, 6]]
    d = DP()
    #print(d.dp_(0, th, 0))
    d.dp2(8, th)