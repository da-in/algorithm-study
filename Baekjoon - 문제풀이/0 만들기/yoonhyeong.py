import copy
from copy import deepcopy

tc = int(input())


def add_operator(tmp):
    if len(tmp) == N - 1:
        arr.append(copy.deepcopy(tmp))
        return

    tmp.append(' ')  # 아스키 코드 34
    add_operator(tmp)
    tmp.pop()

    tmp.append('+')  # 아스키 코드 44
    add_operator(tmp)
    tmp.pop()

    tmp.append('-')  # 아스키 코드 45
    add_operator(tmp)
    tmp.pop()


for _ in range(tc):
    N = int(input())
    arr = []
    add_operator([])

    for i in arr:
        exp = ""
        for j in range(1, N):
            exp += str(j) + str(i[j - 1])
        exp += str(N)

        if eval(exp.replace(' ', '')) == 0:  # 공백 제거(숫자 붙히기)
            print(exp)

    print()