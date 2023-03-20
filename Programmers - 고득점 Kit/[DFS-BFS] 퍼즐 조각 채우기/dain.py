def solution(game_board, table):
    answer = 0
    able_areas = []
    puzzles = []
    l = len(game_board)
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    sx = sy = 0
    dfs_target_number = 0

    def move(puzzle):
        puzzle.sort(key=lambda p: (p[1], p[0]))
        [first_x, first_y] = puzzle[0]
        return list(map(lambda p: (p[0] - first_x, p[1] - first_y), puzzle))

    def rotate(puzzle):
        result = [move(puzzle)]
        for _ in range(3):
            temp = []
            for x, y in result[-1]:
                temp.append((y, -x))
            temp = move(temp)
            result.append(temp)
        return result

    def dfs(matrix, x, y):
        result = []
        matrix[x][y] = (dfs_target_number + 1) % 2
        result.append((x - sx, y - sy))
        for dx, dy in d:
            if 0 <= x + dx < l and 0 <= y + dy < l:
                if matrix[x + dx][y + dy] == dfs_target_number:
                    result += dfs(matrix, x + dx, y + dy)
        return result

    for i in range(l):
        for j in range(l):
            if game_board[i][j] == 0:
                sx = i
                sy = j
                able_areas.append(rotate(dfs(game_board, i, j)))

    dfs_target_number = 1
    for i in range(l):
        for j in range(l):
            if table[i][j] == 1:
                sx = i
                sy = j
                puzzles.append(move(dfs(table, i, j)))

    for puzzle in puzzles:
        for able_area in able_areas:
            if puzzle in able_area:
                able_areas.remove(able_area)
                answer += len(puzzle)
                break

    return answer
