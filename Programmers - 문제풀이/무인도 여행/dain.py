import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    answer = []
    maps = list(map(list, maps))
    r = len(maps)
    c = len(maps[0])

    def dfs(i, j):
        count = int(maps[i][j])
        maps[i][j] = "X"
        if i + 1 < r and maps[i + 1][j] != "X":
            count += dfs(i + 1, j)
        if i - 1 >= 0 and maps[i - 1][j] != "X":
            count += dfs(i - 1, j)
        if j + 1 < c and maps[i][j + 1] != "X":
            count += dfs(i, j + 1)
        if j - 1 >= 0 and maps[i][j - 1] != "X":
            count += dfs(i, j - 1)
        return count

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != "X":
                answer.append(dfs(i, j))
    if not answer:
        answer = [-1]

    return sorted(answer)
