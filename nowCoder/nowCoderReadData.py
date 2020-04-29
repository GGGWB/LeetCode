import sys
n = int(input())
ll = []
for i in range(n):
    sn = list(map(int, input('Please input some numbers:\n').split()))
    ll.append(sn)
print(ll)
# # 应对输入一个行数n，接下来跟着好几行数据的情况，可以读取为列表形式，内部元素是int，注意input敲一次回车结束一行的读取
# # 注：split()函数返回列表
# # map函数，python3返回一个迭代器，应配合list()使用
# # a = list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
# # print(a)
# 可知：sys.stdin.readline().strip() 得到的是一个字符串


# 下面是readline()函数
# -*- coding: utf-8 -*-

# 输入的无论是什么，都会转成字符和字符串
# sys.stdin.readline() 会读取末尾'\n'，加.strip()，去掉回车符，同时去掉前后的空格

# 一
# 输入一个数
n = int(sys.stdin.readline().strip())  # 输入一个元素，并转成整型int
print(n)

# 二
# 输入有n行(已知行数n)，用for循环，一行有任意个字符字符串都可以
seq = []
n = int(input())
for i in range(n):
    line = sys.stdin.readline().strip()  # line此时是字符串列表，不知line有多少个元素
    print(type(line))
    value = map(int, line.split())  # map(函数，列表)Python2.返回列表，Python3.返回迭代器。
    seq += value  # 合并每一行列表
print(seq)
#
# # 三
# # 不确定输入有多少行，用while循环
seq = []
while 1:
    line = sys.stdin.readline().strip()  # line此时是字符串列表，并已去掉前后空格 回车符
    if not line:
        break
    line = map(int, line.split())  # 把line的空格元素去掉，转成字符串列表list，并转成整型int
    seq += line
print(seq)

n = int(input('Please input a number:\n'))
while True:
    sn = list(map(int,input('Please input some numbers:\n').split()))
    if not sn:
        break
    ll.append(sn)


# readlines()
n = int(input())
ll = []
for line in sys.stdin.readlines():
    line = line.strip()
    line = list(map(int, line.split()))
    ll.append(line)
print(ll)