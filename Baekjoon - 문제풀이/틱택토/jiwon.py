import sys

def check_game(g, c):
    # 가로
    if g[0:3]==c*3 or g[3:6]==c*3 or g[6:9]==c*3:
        return True
    
    # 세로
    for i in range(3):
        if g[i]==c and g[i+3]==c and g[i+6]==c:
            return True

    # 대각선
    if g[0]==c and g[4]==c and g[8]==c:
        return True
    if g[2]==c and g[4]==c and g[6]==c:
        return True
    
    return False

while True:
    game = sys.stdin.readline().rstrip('\n')

    if game=='end':
        break

    x_num = game.count('X')
    o_num = game.count('O')

    result_x = check_game(game, 'X')
    result_o = check_game(game, 'O')

    if x_num>o_num+1 or x_num<o_num:
        print("invalid")
        continue

    if result_x and result_o:
        print("invalid")
    elif result_x and x_num==o_num+1:
        print("valid")
    elif result_o and x_num==o_num:
        print("valid")
    elif game.count('.')==0 and x_num==o_num+1:
        print("valid")
    else:
        print("invalid")

