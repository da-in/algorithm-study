def solution(numbers):
    answer = ''
    data=[]
    ck,ck1=0
    for i in numbers:
        if i==1000:
            ck+=1
            continue
        elif i==0:
            ck1+=1
            continue
        i=str(i)        
        
        data.append([i+i*((6-len(i))//len(i)),len(i)])
        
    data.sort(key = lambda x : (-int(x[0]) ))
    
    for i in data:
        answer+=i[0][0:i[1]]
        
    answer+=ck*"1000"+ck1*"0"
        
    return answer if int(answer)>0 else "0"