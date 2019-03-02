# coding=utf-8

import os

fold_name = input("输入备份目录")
target_name = input("输入目标目录")

# 创建备份文件夹
fold = fold_name[fold_name.rfind("/"):]
target_name = target_name + fold

if not os.path.exists(target_name):
    os.mkdir(target_name)

# 切换到目录
os.chdir(fold_name)

files = os.listdir("./")

# 复制文件
for file in files:
    # 如果不是文件 就跳过
    if not os.path.isfile(file):
        continue

    f = open(file, "r")
    ft = open(target_name + "/" + file, "w")
    for line in f.readlines():
        ft.write(line)
    f.close()
    ft.close()

print("完成")
