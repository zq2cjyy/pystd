# coding=utf-8

# 装饰器函数1
def fd1(func):
    print("fd1")

    def inner(*args, **kwargs):
        print("df1-inner")
        return func(*args, **kwargs)

    return inner


# 装饰器函数2
def fd2(func):
    print("fd2")

    def inner(*args, **kwargs):
        print("df2-inner")
        return func(*args, **kwargs)

    return inner


# 被装饰的函数
# 先调用 fd1
# 调用fd1的时候 发现 任然有装饰fd2 于是开始执行fd2 最后执行方法
@fd1
@fd2
def func(a, b, c, d):
    return a + b + c + d


ret = func(1, 2, 3, 4)
print(ret)
