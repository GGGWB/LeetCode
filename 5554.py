f = {'b':1, 'c':7, 'a':4}
g = sorted(f.items(), key=lambda i:i[0])
k = sorted(f.values())
print(k)
print(g)
print(g[0][1])