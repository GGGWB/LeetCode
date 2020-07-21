import os,numpy
l = [11, 2, 3]
k = [4, 5, 6]
l.append(k)
print(l)

music_media = ['compact disc', '8-track tape', 'long playing record']
new_media = ['DVD Audio disc', 'Super Audio CD']
music_media.extend(new_media)
print(music_media)

x = {'age':24, 'sex':'man'}
print(x.get('aa', 'na'))
# print(dir(os))
def doc():
	"这是注释"
	pass
print(doc.__doc__)
class A:
	pass
class B(A):
	pass
print(issubclass(B, B))
t = numpy.arange(12)
x = t.reshape(3, 4)
print(x)
m = {'A', 'B', 'C'}
n = {'B', 'C', 'D'}
print(len(m.intersection(n)))
