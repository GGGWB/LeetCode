a = pow(2, 3)
print(a)
l = [1, 2, 3, 8, 4, 5]
m = max(l)
print(m)
n = sorted(l)
print(n)
joined = ' '.join(str(i) for  i in l)
# j = ' '.join(str(enumerate(l)))
print(joined)
# print(j)
string = 'good my 这是我phyt的 python 我100题面试题python'
string0 = string.center(60)
print(string0)
print(string.find('我'))
print(string.title())
string1 = ['my', 'fisrt', 'python', 'job']
print(' '.join(string1))
print(string.count('python'))
print(l.count(2))
j = [2, 2, 1]
print(l.extend(j))