import sys

# 빌딩층, 자릿수, 반전 LED 수, 실제층
N,K,P,X = map(int, sys.stdin.readline().split())
LED = [
    [1,1,1,0,1,1,1],
    [0,0,1,0,0,1,0],
    [1,0,1,1,1,0,1],
    [1,0,1,1,0,1,1],
    [0,1,1,1,0,1,0],
    [1,1,0,1,0,1,1],
    [1,1,0,1,1,1,1],
    [1,0,1,0,0,1,0],
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,1,1]
]
cnt_dict = dict()
current_led_str = "0" * (K-len(str(X))) + str(X)
current_led = [LED[int(s)] for s in current_led_str]
result = 0

for i in range(1,N+1):
    temp_led_str = "0" * (K-len(str(i))) + str(i)
    if current_led_str==temp_led_str:
        continue
    temp_led = [LED[int(s)] for s in temp_led_str]

    total_cnt = 0
    for j in range(len(current_led)):
        if total_cnt>P:
            break
        if current_led[j]==temp_led[j]:
            continue

        if current_led_str[j]+temp_led_str[j] in cnt_dict:
            total_cnt += cnt_dict[current_led_str[j]+temp_led_str[j]]
            continue

        cnt = 0
        for k in range(7):
            if current_led[j][k]!=temp_led[j][k]:
                cnt+=1
        cnt_dict[current_led_str[j]+temp_led_str[j]] = cnt
        total_cnt+=cnt

    if total_cnt<=P:
        result+=1

print(result)