while True:
    game = input()
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    cnt_o = 0
    cnt_x = 0
    flag = 0

    if game == 'end':
        break

    for i in range(3):
        for j in range(3):
            if game[i * 3 + j] == 'O':
                board[i][j] = -1
                cnt_o += 1
                continue
            if game[i * 3 + j] == 'X':
                cnt_x += 1
                board[i][j] = 1

    # 개수가 안맞는 경우
    if cnt_o > cnt_x or cnt_x - cnt_o > 1:
        print('invalid')
        continue

    # 가로줄 리스트
    col_l = [sum(x) for x in board]
    # 세로줄 리스트
    row_l = [sum(x) for x in [[board[0][0], board[1][0], board[2][0]], [
        board[0][1], board[1][1], board[2][1]], [board[0][2], board[1][2], board[2][2]]]]
    # 대각선
    cross_l = [sum(x) for x in [[board[0][0], board[1][1], board[2][2]], [
        board[0][2], board[1][1], board[2][0]]]]

    # 빙고가 동시에 생기는 경우
    if 3 in col_l and -3 in col_l:
        print('invalid')
        continue

    if 3 in row_l and -3 in row_l:
        print('invalid')
        continue

    # x가 이기는 경우
    if 3 in col_l or 3 in row_l or 3 in cross_l:
        flag = 1
        if cnt_x <= cnt_o:
            print('invalid')
        else:
            print('valid')
        continue

    # o가 이기는 경우
    if -3 in col_l or -3 in row_l or -3 in cross_l:
        flag = 1
        if cnt_x > cnt_o:
            print('invalid')
        else:
            print('valid')
        continue

    # 무승부인 경우
    if flag == 0:
        if cnt_o + cnt_x < 9:
            print('invalid')
        else:
            print('valid')
        continue
