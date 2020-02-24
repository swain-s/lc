# 问题描述：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字
#            b            d
#           j=1  j=2 j=3 j=4
#模板： a  i=1 0   0   0   0
#         i=2 0   0   0   0
#       c i=3 0   0   0   0

class PrinxMatrix(object):
    def __init__(self):
        self.output = []

    def print_matrix(self, matrix):
        for a in matrix:
            print(a)
        print("")

        if matrix == None:
            return []

        elif len(matrix) == 1:
            for num in matrix[0]:
                self.output.append(num)
            return self.output
        elif len(matrix[0]) == 1:
            for arr in matrix:
                self.output.append(arr[0])
            return self.output


        def new_print_matrix(matrix, a, c, b, d):
            print(a, c, b, d)
            if a > c or b > d:
                return self.output
            if a == c and b > d:
                return self.output
            if a > c and b == d:
                return self.output
            if b <= d and a <= c:
                for j in range(b, d+1):
                    self.output.append(matrix[a][j])
                a += 1
            if a <= c and b <= d:
                for i in range(a, c+1):
                    self.output.append(matrix[i][d])
                d -= 1
            if b <= d and a <= c:
                for j in range(d, b-1, -1):
                    self.output.append(matrix[c][j])
                c -= 1
            if a <= c and b <= d:
                for i in range(c, a-1, -1):
                    self.output.append(matrix[i][b])
                b += 1
            return new_print_matrix(matrix, a, c, b, d)
        return new_print_matrix(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1)

if __name__ == "__main__":
    S = PrinxMatrix()
    #print(S.print_matrix([[1, 2, 3], [5, 6, 7], [9, 10, 11], [12, 13, 14]]))
    #print(S.print_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))
    #print(S.print_matrix([[1, 2], [3, 4]]))
    #print(S.print_matrix([[1,2],[3,4],[5,6],[7,8],[9,10]]))
    #print(S.print_matrix([[1], [2], [3], [4], [5]]))
    #print(S.print_matrix([[1]]))
    #print(S.print_matrix([[1, 2, 3, 4]]))

    #for i in range(2, 0, -1):
    #    print(i)