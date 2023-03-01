from collections import defaultdict
def solution(arrows):
    answer = 0
    visit = defaultdict(list)
    x = 0
    y = 0
    dx = [0,1,1,1,0,-1,-1,-1]
    dy = [1,1,0,-1,-1,-1,0,1]

    for arrow in arrows:
        for _ in range(2):
            mx = x + dx[arrow]
            my = y + dy[arrow]  
            
            if (mx, my) in visit and (x, y) not in visit[(mx, my)]:
                answer += 1
                visit[(x, y)].append((mx, my))
                visit[(mx, my)].append((x, y))
            elif (mx, my) not in visit:                  
                visit[(x, y)].append((mx, my))
                visit[(mx, my)].append((x, y))
            x = mx
            y = my 
            
    return answer