n = int(input())
ss = input()
x = []
for s in ss:
    x.append(s)
fangxiang = [[0, 'N', 0], ['W', 0, 'E'], [0, 'S', 0]]
a = [0, 1]
for i in x:
    if i == 'L':
        a[0] += 1
        a[1] -= 1
        fangxiang[0][1], fangxiang[1][0], fangxiang[2][1], fangxiang[1][2] = fangxiang[1][0], fangxiang[2][1], fangxiang[1][2], fangxiang[0][1]
    else:
        a[0] += 1
        a[1] += 1
        fangxiang[0][1], fangxiang[1][0], fangxiang[2][1], fangxiang[1][2] = fangxiang[1][2], fangxiang[0][1], fangxiang[1][0], fangxiang[2][1],
print(fangxiang[0][1])