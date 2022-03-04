def sum(arr, frm, to):
	total = 0;
	for i in range(frm, to + 1):
		total += arr[i]
	return total

def partition(arr, n, k):
	
	# base cases
	if k == 1: # one partition
		return sum(arr, 0, n - 1)
	if n == 1: # one board
		return arr[0]
	best = 100000000
	

	for i in range(1, n + 1):
		best = min(best,
			max(partition(arr, i, k - 1),
						sum(arr, i, n - 1)))
	return best

arr = list(map(int,input().split()))
k = int(input())
n = len(arr)
print(partition(arr, n, k))


