import sys
from itertools import combinations

N = int(sys.stdin.readline())
values = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

total = [i for i in range(N)]
teams = list(combinations(total,N//2))
teams = teams[:len(teams)//2]
result = 100

for team in teams:
    start = list(team)
    link = [i for i in total if i not in start]

    start_comb = list(combinations(start,2))
    start_value = 0
    for i,j in start_comb:
        start_value+=values[i][j]
        start_value+=values[j][i]
    
    link_comb = list(combinations(link,2))
    link_value = 0
    for i,j in link_comb:
        link_value+=values[i][j]
        link_value+=values[j][i]

    result = min(result, abs(start_value-link_value))

print(result)