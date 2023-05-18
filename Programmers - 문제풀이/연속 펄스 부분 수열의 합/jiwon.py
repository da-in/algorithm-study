# def solution(sequence):
#     p_sequence = []
#     m_sequence = []
    
#     for idx in range(len(sequence)):
#         if idx%2==0:
#             p_sequence.append(sequence[idx])
#             m_sequence.append(-sequence[idx])
#         else:
#             p_sequence.append(-sequence[idx])
#             m_sequence.append(sequence[idx])
            
    
#     def max_sum(arr):
#         answer = 0
        
#         start_idx = -1
#         end_idx = -1
        
#         for idx in range(len(arr)-1,-1,-1):
#             if arr[idx]>0:
#                 end_idx = idx
#                 break
        
#         for i in range(len(arr)):
#             temp=0
#             if arr[i]<=0:
#                 pass
#             else:
#                 for j in range(i, end_idx+1):
#                     temp+=arr[j]
#                     if arr[j]<=0:
#                         pass
#                     else:
#                         answer = max(temp, answer)
#         return answer
#        
#    return max(max_sum(p_sequence), max_sum(m_sequence))

def solution(sequence):
    
    def dp(p):
        p_sequence = [i for i in sequence]
        p_sequence[0]*=p
        
        for i in range(1, len(sequence)):
            if i%2==1:
                p_sequence[i] = max(p_sequence[i-1]-p*sequence[i], -p*p_sequence[i])
            else:
                p_sequence[i] = max(p_sequence[i-1]+p*p_sequence[i], p*p_sequence[i])
                
        return max(p_sequence)
    
    start_plus = dp(1)
    start_minus = dp(-1)
    
    answer = max(start_plus, start_minus)
    
    return answer