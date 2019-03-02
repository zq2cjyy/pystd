#!/usr/bin/python3
# -*- coding: UTF-8 -*-

print("lambda 演示")
list = [{"name": "nzq", "age": 10}, {"name": "wdb", "age": 5}, {"name": "mzd", "age": 10}]
print(list)
list.sort(key=lambda x: x["age"])
print(list)
list.sort(key=lambda x: x["name"])
print(list)
list.sort(key=lambda x: (x["age"], x["name"]))
print(list)
list.sort(key=lambda x: x.__getitem__("name"))
print(list)


# 匿名函数作为参数
def sort(list, func):
    list.sort(key=func, reverse=True)


sort(list, lambda x: x["name"])
print(list)

# 字符串变表达式
lstr = '''lambda x: x["age"]'''
lstr = eval(lstr)
sort(list, lstr)
print(list)
