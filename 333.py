import sys
def sell(get, nums):
	res = 0
	day = 1
	for i in range(len(nums)):
		res += get[i]*(day*nums[i]+nums[i]*(nums[i]-1)/2)
		day += nums[i]
	return res


m = int(input())
seq = []
while 1:
	line = sys.stdin.readline().strip()
	if not line:
		break
	line = list(map(int, line.split()))
	seq.append(line)
a = dict()
for i in range(len(seq[0])):
	x = seq[0][i]
	a[x] = seq[1][i]
a = sorted(a.items())
get, nums = [], []
for key, val in a:
	get.append(key)
	nums.append(val)
idx = -1
for i in get:
	if i < 0:
		idx = idx +1

res = sell(get, nums)

print(int(res))

