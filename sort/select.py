# def select_sort(arr):
# 	for i in range(len(arr)-1):  # 剩余未比较个数
# 		minidx = i
# 		for j in range(i+1, len(arr)):  # 可选择范围
# 			if arr[j] < arr[minidx]:
# 				minidx = j
# 		arr[minidx], arr[i] = arr[i], arr[minidx]
# 	return arr
def select_sort(arr):
	for i in range(len(arr)-1):
		minidx = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[minidx]:
				minidx = j
		arr[minidx], arr[i] = arr[i], arr[minidx]
	return arr
x = [1, 8, 2, 6, 0, 7, 9, 2, 4, 7]
b = select_sort(x)
print(b)