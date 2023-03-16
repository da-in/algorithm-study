def solution(rectangle, characterX, characterY, itemX, itemY):
    answer1 = 0
    answer2 = 0
    array = [[0] * 102 for _ in range(102)]
    for x1, y1, x2, y2 in rectangle:
        for x in range(x1 * 2, x2 * 2 + 1):
            for y in range(y1 * 2, y2 * 2 + 1):
                array[x][y] = 1

    for x1, y1, x2, y2 in rectangle:
        for x in range(x1 * 2 + 1, x2 * 2):
            for y in range(y1 * 2 + 1, y2 * 2):
                array[x][y] = 0

    (x, y) = (characterX * 2, characterY * 2)
    while True:
        if (x, y) == (itemX * 2, itemY * 2):
            break
        answer1 += 1
        array[x][y] = 0
        if array[x + 1][y]:
            x += 1
        elif array[x - 1][y]:
            x -= 1
        elif array[x][y + 1]:
            y += 1
        elif array[x][y - 1]:
            y -= 1
        else:
            print("error")
            break

    (x, y) = (itemX * 2, itemY * 2)
    while True:
        if (x, y) == (characterX * 2, characterY * 2):
            break
        answer2 += 1
        array[x][y] = 0
        if array[x + 1][y]:
            x += 1
        elif array[x - 1][y]:
            x -= 1
        elif array[x][y + 1]:
            y += 1
        elif array[x][y - 1]:
            y -= 1
        else:
            print("error")
            break

    return min(answer1, answer2) // 2
