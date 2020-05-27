a = input()
b = input()
for i in b:
    if i >= 'a' and 'i' <= 'z':  # 是字母
        s = chr(ord(i)-ord('a')+ord('A'))  # 转化为大写字母
    else:
        s = i
    if s not in a:
        if '+' not in a or (i < 'A' or i > 'Z'):
            print(i, end="")
# print(ord('a'), ord('A'), ord('0'), ord('1'))