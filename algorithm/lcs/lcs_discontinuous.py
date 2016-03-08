def lcs(left, right):
	left_len = len(left)
	right_len = len(right)
	matrix = [[0 for i in range(right_len+1)] for j in range(left_len+1)]
	flag = [[0 for i in range(right_len+1)] for j in range(left_len+1)]
    
	for i in range(left_len):
		for j in range(right_len):
			if left[i] == right[j]:
				matrix[i+1][j+1] = matrix[i][j]+1
				flag[i+1][j+1] = "ok"
			elif matrix[i+1][j] > matrix[i][j+1]:
				matrix[i+1][j+1] = matrix[i+1][j]
				flag[i+1][j+1] = "left"
			else:
				matrix[i+1][j+1] = matrix[i][j+1]
				flag[i+1][j+1] = "up"
	return matrix,flag

def printLcs(flag, a, i, j):
	if i == 0 or j == 0:
		return
	if flag[i][j] == "ok":
		printLcs(flag, a, i-1, j-1)
		print a[i-1]
	elif flag[i][j] == "left":
		printLcs(flag, a, i, j-1)
	else:
		printLcs(flag, a, i-1, j)
		
a="ABCBDAB"
b="BDCABA"
matrix, flag = lcs(a, b)

for i in matrix:
	print(i)
    
print

for j in flag:
	print j
    
print
printLcs(flag, a, len(a), len(b))
print
