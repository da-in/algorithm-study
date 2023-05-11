def solution(data, col, row_begin, row_end):
    
    data.sort(key=lambda x: (x[col-1], -x[0]))
    answer = sum(map(lambda x: (x % row_begin), data[row_begin-1]))


    for i in range(row_begin+1, row_end+1):
        cal = sum(map(lambda x: (x % i), data[i-1]))
        answer = answer ^ cal
    
    return answer
