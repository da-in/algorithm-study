from itertools import combinations, permutations
n = int(input())

sal = []
people = []
result = 99999

for i in range(n):
    sal.append(list(map(int, input().split(" "))))
    people.append(i)

for team_s in combinations(people, n//2):

    team_l = []
    total_stark = 0
    total_link = 0

    for i in range(n):
        if i not in team_s:
            team_l.append(i)

    for power_s in permutations(team_s, 2):
        total_stark += sal[power_s[0]][power_s[1]]

    for power_l in permutations(team_l, 2):
        total_link += sal[power_l[0]][power_l[1]]

    result = min(result, abs(total_stark - total_link))
print(result)
