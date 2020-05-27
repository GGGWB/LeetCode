import sys

n = int(input())
ll = []
for i in range(n):
	line = sys.stdin.readline().strip()
	line = list(map(int, line.split()))
	ll.append(line)
print(n, ll)