N = int(input())
l = list(input())

red = 0
blue = 0
flag = 0
cnt = []

# 오른쪽으로 레드 모으기
for i in range(N-1, -1, -1):
    if l[i] == 'B':
        flag = 1
    else:
        if flag == 1:
            red += 1
cnt.append(red)

red = 0
flag = 0

# 오른쪽으로 블루 모으기
for i in range(N-1, -1, -1):
    if l[i] == 'R':
        flag = 1
    else:
        if flag == 1:
            blue += 1
cnt.append(blue)

blue = 0
flag = 0

# 왼쪽으로 레드 모으기
for i in range(N):
    if l[i] == 'B':
        flag = 1
    else:
        if flag == 1:
            red += 1
cnt.append(red)
red = 0
flag = 0

# 왼쪽으로 블루 모으기
for i in range(N):
    if l[i] == 'R':
        flag = 1
    else:
        if flag == 1:
            blue += 1
cnt.append(blue)
print(min(cnt))
