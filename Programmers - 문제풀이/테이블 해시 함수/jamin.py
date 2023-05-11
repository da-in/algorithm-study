from functools import reduce

def solution(data, col, row_begin, row_end):
    answer = 0
    S_i = []
    
    data.sort(key = lambda x: (x[col-1],-x[0]))
    
    for i in range(row_begin-1,row_end):
        sum = 0
        for j in range(len(data[0])):
            sum += (data[i][j])%(i+1)
        
        S_i.append(sum)
    
    answer = reduce(lambda x, y: x ^ y, S_i)
    return answer