from itertools import combinations

def calc_meet(l1, l2):
    A, B, E = l1
    C, D, F = l2
    if A * D != B * C:  # 평행하지 않을 경우만 계산
        x = (B * F - E * D) / (A * D - B * C)
        y = (E * C - A * F) / (A * D - B * C)
        return [x, y]


def solution(line):
    meets = []
    pairs = combinations(line, 2)
    for l1, l2 in pairs:
        meet = calc_meet(l1, l2)
        if meet:
            x, y = meet
            if int(x) == x and int(y) == y:
                meets.append([int(x), int(y)])

    xs, ys = zip(*meets)
    minX = min(xs)
    minY = min(ys)
    row = max(xs) - minX
    col = max(ys) - minY
    meets = list(map(lambda x: (x[0] - minX, x[1] - minY), meets))

    # 그리기
    answer = []
    for i in reversed(range(0, col + 1)):
        temp = ""
        for j in range(0, row + 1):
            if (j, i) in meets:
                temp += "*"
            else:
                temp += "."
        answer.append(temp)
    return answer
