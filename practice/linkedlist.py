# def bubble_sort(arr):
# 	for i in range(1, len(arr)):
# 		for j in range(0, len(arr)-i):
# 			if arr[j] > arr[j+1]:
# 				arr[j], arr[j+1] = arr[j+1], arr[j]
# 	return arr
# a = [1,2, 3, 6, 5,4, 0, 22]
# print(bubble_sort(a))

# def insert_sort(arr):
# 	for i in range(len(arr)):
# 		preidx = i-1
# 		cur = arr[i]
# 		while preidx>=0 and arr[preidx] > cur:
# 			arr[preidx+1] = arr[preidx]
# 			preidx-=1
# 		arr[preidx+1] = cur
# 	return arr
# a = [4, 2, 5, 7, 3, 78, 3,0]
# print(insert_sort(a))

# def select_sort(arr):
# 	for i in range(len(arr)-1):
# 		minidx = i
# 		for j in range(i+1, len(arr)):
# 			if arr[j] < arr[minidx]:
# 				minidx = j
# 		arr[minidx], arr[i] = arr[i], arr[minidx]
# 	return arr
# a = [4, 2, 5, 7, 3, 78, 3,0]
# print(select_sort(a))


# def quick_sort(arr):
# 	if len(arr) < 2:
# 		return arr
# 	a = arr[0]
# 	left = [elem for elem in arr[1:] if elem < a]
# 	right = [elem for elem in arr[1:] if elem >=a]
# 	return quick_sort(left) + [a] + quick_sort(right)
# a = [4, 2, 5, 7, 3, 78, 3,0]
# print(quick_sort(a))

def quick_sort(arr, left=None, right=None):
	left = 0 if not isinstance(left, (int, float)) else left
	right = len(arr)-1 if not isinstance(right, (int, float)) else right
	if left < right:
		pi = partition(arr, left, right)
		quick_sort(arr, left, pi-1)
		quick_sort(arr, pi+1, right)
	return arr
def partition(arr, left, right):
	pivot = left
	index = pivot +1
	i = index
	while i <= right:
		if arr[i] < arr[pivot]:
			swap(arr, i, index)
			index+=1
		i+=1
	swap(arr, index-1, pivot)
	return index -1
def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]
a = [4, 2, 5, 7, 3, 36, 78, 3,0]

print(quick_sort(a))