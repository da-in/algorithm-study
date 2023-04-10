def solution(line):
    answer = []
    points = []

    for i in range(len(line)-1) :
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]

            down = a*d - b*c
            up_x = b*f - e*d
            up_y = e*c - a*f
            
            if down == 0:
                continue
                
            x = up_x / down
            y = up_y / down

            if  x == int(x) and y == int(y) :
                x = int(x)
                y = int(y)
                
                points.append([x, y])

    x = list(zip(*points))[0]
    y = list(zip(*points))[1]

    max_x = max(x)
    min_x = min(x)
    max_y = max(y)
    min_y = min(y)

    temp = [['.'] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]

    for x, y in points:
        temp[max_y - y][x - min_x] = '*'

    for line in temp:
        answer.append(''.join(line))
        
    return answer
