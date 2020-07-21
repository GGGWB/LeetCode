import sys
def find_max_time(data, n):
	sum_num = []
	for i in range(n):
		start_time = data[i][1]
		# print('开始')
		# print(start_time)
		nums = data[i][2]
		# print('开始数据')
		# print(nums)
		for j in range(n):
			start_time1 = data[j][1]
			if start_time1 > start_time and start_time1 <= start_time+3600:
				nums += data[j][2]
				# print(start_time1)
				# print(nums)
		sum_num.append(nums)
	
n = int(input())
data = []
while 1:
	line = sys.stdin.readline().strip()
	if not line:
		break
	line = list(map(int, line.split()))
	data.append(line)
find_max_time(data, n)
