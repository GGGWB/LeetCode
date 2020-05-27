# def insert_sort(arr):
# 	for i in range(len(arr)):
# 		preidx = i-1
# 		current = arr[i]
# 		while preidx >= 0 and arr[preidx] > current:
# 			arr[preidx+1] = arr[preidx]
# 			preidx -= 1
# 		arr[preidx+1] = current
# 	return arr
def insert_sort(arr):
	for i in range(len(arr)):
		preidx = i-1
		cur = arr[i]
		while preidx >= 0 and arr[preidx] > cur:
			arr[preidx+1] = arr[preidx]
			preidx -= 1
		arr[preidx+1] = cur
	return arr



a = [1, 3, 5, 9, 6, 8, 0]
b = insert_sort(a)
print(b)