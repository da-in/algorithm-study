import sys

N,D = map(int, input().split())
road_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
road_list.sort(key = lambda x:x[1])
road_distance = [i for i in range(D+1)]

for i in range(D+1):
    road_distance[i] = min(road_distance[i], road_distance[i-1]+1)

    for j in range(N):
        if i==road_list[j][1]:
            road_distance[i] = min(road_distance[i], road_distance[road_list[j][0]]+road_list[j][2])

print(road_distance[D])