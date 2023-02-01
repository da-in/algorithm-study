def solution(name):
    name_len = len(name)
    change = []
    move = []

    # change : 인덱스별 알파벳 수정 횟수
    # move : 방문해야할 인덱스들의 거리 튜플 (왼쪽에서 갈 경우, 오른쪽에서 갈 경우)로 저장
    for i in range(name_len):
        c = min(ord(name[i]) - ord("A"), ord("Z") - ord(name[i]) + 1)
        change.append(c)
        if i == 0:
            move.append((0, 0))  # 0번째 인덱스는 변경 여부와 관계 없이 무조건 move에 추가해야함.
            continue
        if c:
            move.append((i, (name_len - i) % name_len))

    # 수정하지 않아도 될 경우
    if not sum(change):
        return 0

    move_len = len(move)
    min_move = name_len  # 최소 이동 횟수, 일단 이름 길이로 초기화

    for i in range(move_len):
        right_first = move[i][0] + move[(i + 1) % move_len][1] * 2
        left_first = move[i][0] * 2 + move[(i + 1) % move_len][1]
        min_move = min(min_move, right_first, left_first)

    return sum(change) + min_move
