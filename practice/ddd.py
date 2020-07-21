n = int(input())
ll=[]
while True:
	line = list(map(int, input().strip().split()))
	if not line:
		break
	ll.append(line)
print(n, ll)