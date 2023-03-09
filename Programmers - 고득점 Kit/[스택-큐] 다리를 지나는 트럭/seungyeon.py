def main():
    print(solution(2,10,[7,4,5,6]))

def solution(bridge_length, weight, truck_weights):
    
    answer = 0
    que = [0 for _ in range(bridge_length)]
    
    while que:
        
        answer += 1
        que.pop(0)
        
        if truck_weights:
            if sum(que) + truck_weights[0] <= weight:            
                t = truck_weights.pop(0)
                que.append(t)
            else:
                que.append(0)
                 
         
    return answer

# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     que = []
#     i=total=0
#     que.append(truck_weights[0])
#     while(que and i < len(truck_weights)):
#         que.append(truck_weights[i])
#         total += truck_weights[i]

#         answer+=1
#         if len(que) == bridge_length and total <= weight:
#             que.clear
#         i+=1    
#         # que.append(truck_weights[i])
#         answer+=1

#     return answer
    
if __name__ == "__main__":
    main()