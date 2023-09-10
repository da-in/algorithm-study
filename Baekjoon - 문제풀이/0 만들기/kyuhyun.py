N = int(input())

def cal(cur_num, n):
    if cur_num == res_num + 1:
        res(n)
        return
    
    cal(cur_num + 1, n + ' ' + str(cur_num))
    cal(cur_num + 1, n + '+' + str(cur_num))
    cal(cur_num + 1, n + '-' + str(cur_num))

def res(n):
    st = n.replace(' ', '')
    if eval(st) == 0:
        print(n)

for _ in range(N):
    global res_num
    res_num = int(input())
    cal(2, '1')
    print()
