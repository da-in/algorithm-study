def solution(line):
    answer = []
    temp = []
    
    for i in range(len(line)):
        a,b,e = line[i]
        for c,d,f in line[i+1:]:
            if a*d-b*c == 0:
                continue
            x = (b*f-e*d)/(a*d-b*c)
            y = (e*c-a*f)/(a*d-b*c)
            
            if x==int(x) and y==int(y):
                x,y = map(int,[x,y])
                    
                if [x,y] not in temp:
                    temp.append([x,y])
    min_x, max_x = min(temp, key=lambda x: x[0])[0], max(temp, key=lambda x: x[0])[0]
    min_y, max_y = min(temp, key=lambda x: x[1])[1], max(temp, key=lambda x: x[1])[1]
                
    temp.sort(key=lambda x:-x[1])
    last_y = (temp[0])[1]
    
    for x,y in temp:
        while last_y-y>1:
            answer.append('.'*(max_x-min_x+1))
            last_y-=1
        if last_y==y and answer:
            pop = answer.pop()
            answer.append(pop[:x-min_x]+'*'+pop[x-min_x+1:])
        else:
            answer.append('.'*(x-min_x)+'*'+'.'*(max_x-x))
        last_y=y
    
    
    return answer