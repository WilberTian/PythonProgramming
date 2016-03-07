def lcs(left, right):
    left_len = len(left)
    right_len = len(right)
    
    matrix = [[0 for col in range(right_len)] for row in range(left_len)]
    max_len = 0
    end = 0
    
    for i in range(left_len):
        for j in range(right_len):
            if left[i] == right[j]:
                if i == 0 or j == 0:
                    matrix[i][j] = 1
                else:
                    matrix[i][j] = matrix[i-1][j-1] + 1
            else:
                matrix[i][j] = 0
                
            if matrix[i][j] > max_len:
                max_len = matrix[i][j]
                end = i
                
    print matrix
    print "max length of sub string is", max_len
    print end
    print left[(end-max_len+1):(end+1)]
    
lcs("21232523311324", "312123223445")    