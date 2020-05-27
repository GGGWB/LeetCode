def bubble_sort(arr):
	for i in range(1, len(arr)):
		for j in range(0, len(arr)-1):
			if arr[j] > arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
	return arr
a = [1, 2, 6, 5, 9, 0]
b = bubble_sort(a)
print(b)