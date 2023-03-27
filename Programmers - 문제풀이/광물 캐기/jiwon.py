def solution(picks, minerals):
    if picks[0]*5>len(minerals):
        return len(minerals)
    if sum(picks)*5<len(minerals):
        idx=len(minerals)-sum(picks)*5
        minerals=minerals[:-idx]
    
    answer = 0
    l=[0 for i in range(len(minerals)//5+1)]
    l_stack=[]
    p_str=[]
    
    for i in range(len(minerals)):
        if minerals[i]=="diamond":
            l[i//5] += 25
        elif minerals[i]=="iron":
            l[i//5] += 5
        else:
            l[i//5] += 1
            
    sort_l = sorted(l)
    
    for i in range(len(sort_l)):
        idx = l.index(sort_l[i])
        start_idx = idx*5
        end_idx = start_idx+5
        l[idx] = -1
        temp_list=[]
        
        if end_idx-1 > len(minerals):
            end_idx = len(minerals)
        
        for i in range(start_idx,end_idx):
            temp_list.append(minerals[i])
        l_stack.append(temp_list)
        
    for i in range(len(picks)):
        while picks[i]:
            if i==0:
                p_str.append('diamond')
            elif i==1:
                p_str.append('iron')
            else:
                p_str.append('stone')
            picks[i]-=1

            
    for i in range(len(l_stack)):
        for j in l_stack.pop():
            if p_str[0]=='diamond':
                answer+=1
            elif p_str[0]=='iron':
                if j=='diamond':
                    answer+=5 
                else:
                    answer+=1
            else:
                if j=='diamond':
                    answer+=25
                elif j=='iron':
                    answer+=5
                else:
                    answer+=1
        p_str.remove(p_str[0])
        if len(p_str)==0:
            break
    
    return answer