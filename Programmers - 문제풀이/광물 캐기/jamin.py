def solution(picks, minerals):
    answer = 0
    
    total_picks = 0 #곡괭이 총 갯수
    stone_energy = {"diamond":25, "iron":5, "stone":1}
    energy = {"diamond": [1, 5, 25], "iron": [1, 1, 5], "stone": [1, 1, 1]}
    # index = {"diamond": 0, "iron": 1, "stone": 2}
    for i in range (len(picks)):
        total_picks += picks[i]
    
    total_minerals = min(total_picks*5,len(minerals))


    temp = []
    count = 0
    worst_energy = 0
    energy_list = []
    for i in range (total_minerals):
        worst_energy += stone_energy[minerals[i]]   #돌 피로도(최악)
        temp.append(minerals[i]) #diamond,iron,diamond...
        count += 1
        if count >=5:
            worst_energy = 0
            count = 0
            energy_list.append([worst_energy,temp])
    if worst_energy:    #5의 배수 아니었을 때 남은 광물
        energy_list.append([worst_energy,temp])  
        
    energy_list.sort(key = lambda x:-x[0]) #피로도 높은 순으로 정렬 [85,[d,d,d,i,i]]

    # for i,lst in enumerate(energy_list): #i=0,1,2.. lst=[85,[d,d,d,i,i]]..
    #     picks_index = index[picks[i]]
    #     for j in range(len(lst[1])): #j=0,1,2...광물 갯수
    #         answer += energy[lst[1][j]][picks_index]
        

    return answer

solution([1, 3, 2],["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])