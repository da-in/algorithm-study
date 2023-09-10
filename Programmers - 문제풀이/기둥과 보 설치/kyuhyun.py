def col_check(col_visit, bo_visit, x, y):
    if y == 0 or col_visit[x][y-1]:
        return True
    if (x > 0 and bo_visit[x-1][y] ) or bo_visit[x][y]:
        return True
    return False

def bo_check(col_visit, bo_visit, x, y):
    if col_visit[x][y-1] or col_visit[x+1][y-1]:
        return True
    if x > 0 and bo_visit[x-1][y] and bo_visit[x+1][y]:
        return True
    return False
    
def remove_col_check(col_visit, bo_visit, x, y):
    
    if bo_visit[x-1][y+1] and not bo_check(col_visit, bo_visit, x-1, y+1):
        return False
    if bo_visit[x][y+1] and not bo_check(col_visit, bo_visit, x, y+1):
        return False
    if col_visit[x][y+1] and not col_check(col_visit, bo_visit, x, y+1):
        return False
    return True

def remove_bo_check(col_visit, bo_visit, x, y) :
    if bo_visit[x-1][y] and not bo_check(col_visit, bo_visit, x-1, y):
        return False
    if bo_visit[x+1][y] and not bo_check(col_visit, bo_visit, x+1, y):
        return False
    if col_visit[x][y] and not col_check(col_visit, bo_visit, x, y):
        return False
    if col_visit[x+1][y] and not col_check(col_visit, bo_visit, x+1, y):
        return False
    return True

def solution(n, build_frame):
    answer = []
    col_visit = [[0 for _ in range(n+1)] for _ in range(n+1)]
    bo_visit = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for val in build_frame:
        x, y, kind, act = val
        # 기둥인 경우
        if kind == 0:
            # 설치
            if act == 1:
                if col_check(col_visit, bo_visit, x, y):
                    col_visit[x][y] = 1
                    answer.append([x, y, kind])
            # 삭제
            else:
                col_visit[x][y] = 0
                if not remove_col_check(col_visit, bo_visit, x, y):
                    col_visit[x][y] = 1
                else:
                    answer.remove([x, y, kind])

        # 보인 경우
        else:
            # 설치
            if act == 1:
                if bo_check(col_visit, bo_visit, x, y) :
                    bo_visit[x][y] = 1
                    answer.append([x, y, kind])
            # 삭제
            else:
                bo_visit[x][y] = 0
                if not remove_bo_check(col_visit, bo_visit, x, y):
                    bo_visit[x][y] = 1
                else:
                    answer.remove([x, y, kind])
                    
    answer.sort()
    return answer
