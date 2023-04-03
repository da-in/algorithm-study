def cal_start(start):
    time = list(map(int,start.split(":")))
    total = time[0]*60 + time[1]
    return total
    
def solution(plans):
    answer = []
    stack = []
    plans.sort(key = lambda plans:plans[1])
    print(plans)
    
    for name,start,playtime in plans:
        start = cal_start(start)
        playtime = int(playtime)
        
        if stack:
            pre_name, pre_start, pre_playtime = stack.pop()
            total = start - pre_start  
              
            if total < pre_playtime:
                pre_playtime -= total
                stack.append((pre_name,pre_start,pre_playtime))
                
            else:   #total>=playtime
                answer.append(pre_name)
                total -= pre_playtime
                if stack:
                    if total>pre_playtime:
                        
                        pre_name, pre_start, pre_playtime = stack.pop()

                        total = start - pre_start
                        if total < pre_playtime:
                            pre_playtime -= total
                            stack.append((pre_name,pre_start,pre_playtime))
                        else:
                            answer.append(pre_name)
                            total -= pre_playtime
                
        stack.append((name,start,playtime))
        
    print(stack)
    for i in range(len(stack)):
        remain = stack.pop()
        answer.append(remain[0])
    return answer

# # def end(plans):
# #     time = plans[1].split(':')
# #     time = list(map(int,time))
# #     plans[2] = int(plans[2])
# #     time[1]+=plans[2]
# #     if plans[2]>=60:
# #         time[0]+=plans[2]//60
# #         time[1] = plans[2]%60
# #     return str(time[0])+":"+str(time[1])   

# def cal(plans1,plans2):
#     result = 1
#     time1 = plans1[1].split(':')
#     time1 = list(map(int,time1))
#     time2 = plans2[1].split(':')
#     time2 = list(map(int,time2))
#     if time1[1]<time2[1]:
#         time1[0] -=1
#         time1[1] += 60
#     time1[0] -= time2[0]
#     time1[1] -= time2[1]
    
#     result = time1[0]*60+time1[1]

#     #print("시간차이: ",result)
    
#     return result

# def solution(plans):
#     answer = []
#     keep = []
#     restart = []
#     plans.sort(key=lambda plans:plans[1])
#     #print(plans)
#     for i in range(len(plans)-1):
#         if cal(plans[i+1],plans[i])<int(plans[i][2]):
#             plans[i][2] =str(int(plans[i][2])-cal(plans[i+1],plans[i])) 
#             keep.append(plans[i])
            
#         elif cal(plans[i+1],plans[i])>int(plans[i][2]):
#             answer.append(plans[i][0])
#             restart = keep.pop()
#             plans[i]=restart
#             solution(plans)
#         else:
#             answer.append(plans[i][0])
#     answer.append(plans[i+1][0])
#     for i in range(len(keep)):
#         restart = keep.pop()
#         answer.append(restart[0])
        
#    # print(keep) 
#     return answer