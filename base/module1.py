#coding=utf-8
def sum(i, j):
    return i + j


# 运行 module2 不会打印下边的语句 因为当前的module __name__ 为module1
# 直接运行module1 会打印
if __name__ == '__main__':
    print('module1')
