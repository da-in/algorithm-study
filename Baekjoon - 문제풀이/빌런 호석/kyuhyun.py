N, K, P, X = map(int, input().split(" "))

num_list = []
res = 0

num_list.append([1,1,1,1,1,1,0]) #0
num_list.append([0,0,1,1,0,0,0]) #1
num_list.append([0,1,1,0,1,1,1]) #2
num_list.append([0,1,1,1,1,0,1]) #3
num_list.append([1,0,1,1,0,0,1]) #4
num_list.append([1,1,0,1,1,0,1]) #5
num_list.append([1,1,0,1,1,1,1]) #6
num_list.append([0,1,1,1,0,0,0]) #7
num_list.append([1,1,1,1,1,1,1]) #8
num_list.append([1,1,1,1,1,0,1]) #9

# 두 숫자간의 패널 수 차이를 구하는 함수
def diff_one(num1, num2) :
    cnt = 0
    for i in range(7):
        if num_list[num1][i] != num_list[num2][i]:
            cnt += 1
    return cnt

#두 수간의 총 차이 구하기
def diff_num(num1, num2) :
    led = 0
    for i in range(K):
        led += diff_one(num1 % 10, num2 % 10)
        num1 = num1 // 10
        num2 = num2 // 10
    return led

for val in range(1, N+1):
    if val == X:
        continue
    if diff_num(X, val) <= P :
        res += 1
print(res)
