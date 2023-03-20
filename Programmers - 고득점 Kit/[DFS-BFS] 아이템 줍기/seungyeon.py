from collections import deque


def main():
    print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]],1,3,7,8))


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    field = [[-1] * 102 for i in range(102)]
    
    for r in rectangle:
        # 모든 좌표값 2배
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # 직사각형 내부
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                # 직사각형의 테두리
                elif field[i][j] != 0:
                    field[i][j] = 1
                    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append([characterX * 2, characterY * 2])

    visited = [[1] * 102 for i in range(102)]

    visited[characterX * 2][characterY * 2] = 0 
    
    while q:
        x, y = q.popleft()
        
        # 도착
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            # 현재 좌표가 테두리이고 아직 방문하지 않은 곳이라면 q에 추가 후 visited를 최단거리로 갱신
            if field[nx][ny] == 1 and visited[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    
    return answer
    
if __name__ == "__main__":
    main()
