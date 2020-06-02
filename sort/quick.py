# def quick_sort(arr):
# 	if len(arr)<2:
# 		return arr
# 	a = arr[0]
# 	left = [elem for elem in arr[1:] if elem <= a]
# 	right = [elem for elem in arr[1:] if elem > a]
# 	return quick_sort(left) + [a] + quick_sort(right)

# def quick_sort(arr):
# 	if len(arr)<2:
# 		return arr
# 	a = arr[0]
# 	left = [elem for elem in arr[1:] if elem < a]
# 	right = [elem for elem in arr[1:] if elem >= a]
# 	return quick_sort(left) + [a] + quick_sort(right)
 
# def quick_sort(arr, left=None, right=None):
# 	left = 0 if not isinstance(left, (int, float)) else left
# 	right = len(arr)-1 if not isinstance(right, (int, float)) else right
# 	if left < right:
# 		idx = partition(arr, left, right)
# 		quick_sort(arr, left, idx-1)
# 		quick_sort(arr, idx+1, right)
# 	return arr
#
# def partition(arr, left, right):
# 	privot = left
# 	index = privot + 1
# 	i = index
# 	while i <= right:
# 		if arr[i] < arr[privot]:
# 			swap(arr, index, i)
# 			index+=1
# 		i += 1
# 	swap(arr, privot, index-1)
# 	return index-1
#
# def swap(arr, i, j):
# 	arr[i], arr[j] = arr[j], arr[i]
#
# def quick_sort(arr):
# 	if len(arr) < 2:
# 		return arr
# 	a = arr[0]
# 	left = [elem for elem in arr[1:] if elem <= a]
# 	right = [elem for elem in arr[1:] if elem > a]
# 	return quick_sort(left) + [a] + quick_sort(right)
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
	index = pivot+1
	i = index
	while i <= right:
		if arr[i] < arr[pivot]:
			arr[i], arr[index] = arr[index], arr[i]
			index += 1
		i += 1
	arr[pivot], arr[index-1] = arr[index-1], arr[pivot]
	return index-1



x = [1, 8, 2, 6, 0, 7, 9, 2, 4, 7]
b = quick_sort(x)
print(b)