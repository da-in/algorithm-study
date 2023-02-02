def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    cm = lost & reserve
    lost = sorted(lost-cm)
    reserve = sorted(reserve-cm)
    while lost and reserve:
        r = reserve.pop(0)
        for i in [-1, 1]:
            if r+i in lost:
                lost.remove(r+i)
                break
    return n-len(lost)