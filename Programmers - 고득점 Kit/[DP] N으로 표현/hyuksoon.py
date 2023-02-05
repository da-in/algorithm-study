def solution(N, number):
    if N==number:
        return 1
    data=[[] for i in range(9)]
    
    data[1]=[N]
    
    for i in range(2,9):
        data[i].append(int(str(N)*i))
        for j in range(1,(i//2)+1):
            for d in data[j]:
                for t in data[i-j]:
                    data[i].append(d+t)
                    data[i].append(d*t)
                    if d-t>0:
                        data[i].append(d-t)
                    if t-d>0:
                        data[i].append(t-d)
                    if d//t>0:
                        data[i].append(d//t)
                    if t//d>0:
                        data[i].append(t//d)
        if number in data[i]:
            return i
    


    return -1
