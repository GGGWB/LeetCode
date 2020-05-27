#coding=utf-8
import sys
#str = input()
#print(str)



str1 = '12345{safsdf（dafadsf)ddd([sdfs]}'

a = []
for i in str1:
	if i in ('{', '(', '['):
		a.append(i)
		continue
	if i == '}':
		if a[-1] == '{':
			a.pop()
			print('{}')
			continue
	if i == ']':
		if a[-1] == '[':
			a.pop()
			print('[]')
			continue
	if i == ')':
		if a[-1] == '(':
			a.pop()
			print('()')
			continue
