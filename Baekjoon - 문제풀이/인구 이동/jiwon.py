import sys

N, L, R = map(int, input().split())

people_list = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]

def move_people():
    dif_idx_list = [[]]
    dif_sum_list = []

    for i in range(len(people_list)):
        for j in range(len(people_list[i])):
            # 상 하 좌 우 인구차 탐색
            DOWN, RIGHT = -1, -1

            if i==N-1:
                pass
            else:
                DOWN = max(people_list[i][j], people_list[i+1][j]) - min(people_list[i][j], people_list[i+1][j])
                if DOWN<L or DOWN>R:
                    DOWN = -1

            # if j==0:
            #     pass
            # else:
            #     LEFT = dif_list[i][j-1][3]
            
            if j==N-1:
                pass
            else:
                RIGHT = max(people_list[i][j], people_list[i][j+1]) - min(people_list[i][j], people_list[i][j+1])
                if RIGHT<L or RIGHT>R:
                    RIGHT = -1
            
            # dif_list[i][j] = [UP, DOWN, LEFT, RIGHT]
            if DOWN!=-1:
                is_in = False
                
                for x in range(len(dif_idx_list)):
                    if is_in:
                        break
                    if len(dif_idx_list[0])==0:
                        is_in = True
                        dif_idx_list[0].append((i,j))
                        dif_idx_list[0].append((i+1,j))
                        dif_sum_list.append(sum([people_list[i][j], people_list[i+1][j]]))
                        continue
                    for (i1,j1) in dif_idx_list[x]:
                        if [i,j]==[i1,j1] and (i+1,j) not in dif_idx_list[x]:
                            is_in = True
                            dif_idx_list[x].append((i+1,j))
                            dif_sum_list[x]+=people_list[i+1][j]
                            break
                        elif [i+1,j]==[i1,j1] and (i,j) not in dif_idx_list[x]:
                            is_in = True
                            dif_idx_list[x].append((i,j))
                            dif_sum_list[x]+=people_list[i][j]
                            break
                if not is_in:
                    dif_idx_list.append([])
                    dif_idx_list[-1].append((i,j))
                    dif_idx_list[-1].append((i+1,j))
                    dif_sum_list.append(sum([people_list[i][j], people_list[i+1][j]]))

            if RIGHT!=-1:
                is_in = False
                for x in range(len(dif_idx_list)):
                    if is_in:
                        break
                    if len(dif_idx_list[0])==0:
                        is_in = True
                        dif_idx_list[0].append((i,j))
                        dif_idx_list[0].append((i,j+1))
                        dif_sum_list.append(sum([people_list[i][j], people_list[i][j+1]]))
                        continue
                    for (i1,j1) in dif_idx_list[x]:
                        if [i,j]==[i1,j1] and (i,j+1) not in dif_idx_list[x]:
                            is_in = True
                            dif_idx_list[x].append((i,j+1))
                            dif_sum_list[x]+=people_list[i][j+1]
                            break
                        elif [i,j+1]==[i1,j1] and (i,j) not in dif_idx_list[x]:
                            is_in = True
                            dif_idx_list[x].append((i,j))
                            dif_sum_list[x]+=people_list[i][j]
                            break
                if not is_in:
                    dif_idx_list.append([])
                    dif_idx_list[-1].append((i,j))
                    dif_idx_list[-1].append((i,j+1))
                    dif_sum_list.append(sum([people_list[i][j], people_list[i][j+1]]))

    if len(dif_idx_list[0])==0:
        return False

    for idx, l in enumerate(dif_idx_list):
        for (i1,j1) in l:
            people_list[i1][j1] = dif_sum_list[idx]//len(l)

    print(dif_idx_list)
    print(people_list)
    print(dif_sum_list)

    return True

# print(dif_idx_list)
# print(dif_sum_list)

answer = 0
while move_people():
    answer+=1

print(answer)