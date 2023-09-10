import sys

MAX_Y = 500001
N = int(sys.stdin.readline())
y_list = []
result = 0

for _ in range(N):
    x,y = map(int, sys.stdin.readline().split())

    if y!=0 and y not in y_list:
        y_list.append(y)
        result+=1
    
    temp_list = []
    for i in y_list:
        if i<=y:
            temp_list.append(i)
    y_list = temp_list
    

print(result)