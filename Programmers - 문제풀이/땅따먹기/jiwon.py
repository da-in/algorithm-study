def solution(land):
#     answer = 0
#     idx = -1
    
#     for i in land:
#         if idx!=-1:
#             i[idx]=-1
#         m=max(i)
#         answer+=m
#         idx=i.index(m)

    for i in range(1, len(land)):
        for j in range(4):
            temp=(land[i-1])[j]
            (land[i-1])[j]=-1
            (land[i])[j]+=max(land[i-1])
            (land[i-1])[j]=temp
            
    answer=max(land[-1])
    
    return answer