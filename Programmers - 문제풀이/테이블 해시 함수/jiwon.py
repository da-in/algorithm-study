def solution(data, col, row_begin, row_end):
    answer=0
    data.sort(key=lambda x: (x[col-1],-x[0]))
    
    for i in range(row_begin-1, row_end):
        temp=0
        for j in data[i]:
            temp+=j%(i+1)
        answer = answer^temp
    
    return answer