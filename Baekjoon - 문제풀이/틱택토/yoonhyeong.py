import sys


def count_ch(ch):  # 특정 문자 갯수 반환
    count = 0

    for row in board:
        count += row.count(ch)

    return count


def check_row(ch):  # 가로 3칸 완성

    for i in range(0, 3):
        if board[i][0] == board[i][1] == board[i][2] == ch:
            if board[i][0] == 'X':
                return True
            elif board[i][0] == 'O':
                return True

    return False


def check_column(ch):  # 세로 3칸 완성

    for i in range(0, 3):
        if board[0][i] == board[1][i] == board[2][i] == ch:
            if board[0][i] == 'X':
                return True
            elif board[0][i] == 'O':
                return True

    return False


def check_cross(ch):  # 대각선 3칸 완성

    if board[0][0] == board[1][1] == board[2][2] == ch:
        if board[0][0] == 'X':
            return True
        elif board[0][0] == 'O':
            return True

    if board[0][2] == board[1][1] == board[2][0] == ch:
        if board[0][2] == 'X':
            return True
        elif board[0][2] == 'O':
            return True

    return False


while True:
    str = input()

    if str == 'end':
        break

    else:
        index = 0
        board = [['' for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                board[i][j] = str[index]
                index += 1

        if count_ch('X') < count_ch('O'):
            print("invalid")
            continue
        if count_ch('X') > count_ch('O') + 1:
            print("invalid")
            continue

        if count_ch('X') == 5 and count_ch('O') == 4:
            print("valid")
            continue

        if count_ch('X') == count_ch('O'):
            if (check_row('O') and not check_row('X')) or (check_column('O') and not check_column('X')) or (
                    check_cross('O') and not check_cross('X')):
                print("valid")
                continue

        if count_ch('X') == count_ch('O') + 1:
            if (check_row('X') and not check_row('O')) or (check_column('X') and not check_column('O')) or (
                    check_cross('X') and not check_cross('O')):
                print("valid")
                continue

        print("invalid")
