# selection sort program impletation in python

def sort(arr):
	while True:
		for i in range(5):
			minpos = i
			for j in range(i, 5):
				if arr[j] < arr[minpos]:
					minpos = j


			temp = arr[i]
			arr[i] = arr[minpos]
			arr[minpos] = temp



# best 0(n)
print(sort([1, 12, 8, 5, 25]))
# average 0(n^2)                
print(sort([4, 2, 3, 1, 6, 5]))
# worst 0(n^2)
print(sort([6, 5, 4, 3, 2, 1]))
