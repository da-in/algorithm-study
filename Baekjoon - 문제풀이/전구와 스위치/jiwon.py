import sys

N = map(int, input())
from_bulb = list(map(int, sys.stdin.readline().rstrip('\n')))
to_bulb = list(map(int, sys.stdin.readline().rstrip('\n')))

def switchBulb(f, t):
    # 값만 복사
    F = f[:]
    switch = 0
    for i in range(1, len(F)):
        if F[i-1]==t[i-1]:
            pass
        else:
            F[i-1] = 1-F[i-1]
            F[i] = 1-F[i]
            if i<len(F)-1:
                F[i+1] = 1-F[i+1]
            switch+=1
    return switch if F==t else 1e9

# 첫번째 전구를 누르지 않은 경우
result1 = switchBulb(from_bulb, to_bulb)
# 첫번째 전구를 누르지 않은 경우
from_bulb[0] = 1-from_bulb[0]
from_bulb[1] = 1-from_bulb[1]
result2 = switchBulb(from_bulb, to_bulb)+1

if result1==1e9 and result2==1e9+1:
    print(-1)
else:
    print(min(result1, result2))