def solution(plans):
    answer=[]
    p_stack=[]
    plans.sort(key=lambda x:x[1])
    
    for sub, clock, time in plans:
        h,m = map(int, clock.split(":"))
        clock = h*60+m
        time = int(time)
        if p_stack:
            s_sub, s_clock, s_time = p_stack.pop()
            left_time = clock-s_clock
            if left_time<s_time:
                s_clock = clock
                s_time -= left_time
                print(s_sub, s_time)
                p_stack.append([s_sub, s_clock, s_time])
            else:
                answer.append(s_sub)
                while p_stack and left_time>0:
                    temp_clock = s_clock+s_time
                    s_sub, s_clock, s_time = p_stack.pop()
                    s_clock = temp_clock
                    left_time = clock-s_clock
                    if left_time<s_time:
                        s_clock = clock
                        s_time -= left_time
                        p_stack.append([s_sub, s_clock, s_time])
                        break
                    else:
                        answer.append(s_sub)
                        
        p_stack.append([sub,clock,time])
        
    for sub,_,_ in p_stack[::-1]:
        answer.append(sub)
    
    return answer
