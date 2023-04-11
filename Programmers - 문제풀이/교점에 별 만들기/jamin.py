

import itertools
def solution(line):
    answer = []
    points = []
    integers = []
    
    
    #print(ncr)
    # for i in ncr:
    #     x = (i[0][1]
    #     points.append([])
    
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a = line[i][0]
            b = line[i][1]
            e = line[i][2]
            c = line[j][0]
            d = line[j][1]
            f = line[j][2]
            
            if (a*d-b*c)==0:
                continue
                
            x = (b*f-e*d) / (a*d-b*c)
            y = (e*c-a*f) / (a*d-b*c)
            points.append([x,y])
            
    for i in points:
        if i[0].is_integer() and i[1].is_integer():
            i[0] = int(i[0])
            i[1] = int(i[1])
            integers.append(i)

    
    row_max = max(list(zip(*integers))[0])
    row_min = min(list(zip(*integers))[0])
    col_max = max(list(zip(*integers))[1])
    col_min= min(list(zip(*integers))[1])
            
    arr = [["." for j in range(int(row_max-row_min)+1)] for i in range(int(col_max-col_min)+1)]

    
    # for i in range(len(arr)):
    #     for j in range(len(arr[i])):
    #         print(arr[i][j])
    # print(integers)
    
    for i in integers:
        x = i[0] - row_min
        y = col_max - i[1]
        # i = [y,x]
        # print(i)
        arr[y][x] = '*'

    
    for i,j in enumerate(arr):
        answer.append(''.join(j))
    #     print(i,arr[i])
    # print(answer)
        
    return answer