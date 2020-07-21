def quickSort(arr, l=None, r=None):
	l = 0 if not isinstance(l, (int, float)) else l
	r = len(arr)-1 if not isinstance(r, (int, float)) else r
	if l < r:
		partnum = partition(arr, l, r)
		quickSort(arr, l, partnum-1)
		quickSort(arr, partnum+1, r)
	return arr


def partition(arr, l, r):
	privit = l
	index = privit+1
	i = index
	while i <= r:
		if arr[i] < arr[privit]:
			swap(arr, i, index)
			index+=1
		i+=1
	swap(arr, privit, index-1)
	return index-1
def swap(arr, i, j):
	arr[i], arr[j] = arr[j], arr[i]


print(quickSort([7,6,5,4,3,2,1]))


