# def quick_sort(arr, left=None, right=None):
# 	left = 0 if not isinstance(left, (int, float)) else left
# 	right = len(arr)-1 if not isinstance(right, (int, float)) else right
# 	if left < right:
# 		pi = partition(arr, left, right)
# 		quick_sort(arr, left, pi-1)
# 		quick_sort(arr, pi+1, right)
# 	return arr
# def partition(arr, left, right):
# 	pivot = left
# 	index = pivot + 1
# 	i = index
# 	while i <= right:
# 		if arr[i] < arr[pivot]:
# 			arr[i], arr[index] = arr[index], arr[i]
# 			index += 1
# 		i += 1
# 	arr[pivot], arr[index-1] = arr[index-1], arr[pivot]
# 	return index-1


def quick_sort(arr, left=None, right=None):
	left = 0 if not isinstance(left, (int, float)) else left
	right = len(arr)-1 if not isinstance(right, (int, float)) else right
	if left < right:
		ref = partition(arr, left, right)
		quick_sort(arr, left, ref-1)
		quick_sort(arr, ref+1, right)
	return arr
def partition(arr, left, right):
	pivot = left
	index = pivot + 1
	i = index
	while i <= right:
		if arr[i] < arr[pivot]:
			arr[index], arr[i] = arr[i], arr[index]
			index += 1
		i += 1
	arr[pivot], arr[index-1] = arr[index-1], arr[pivot]
	return index-1

a = [9, 2, 4, 6, 7, 1, 0, 22]
print(quick_sort(a))
