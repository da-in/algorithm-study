import sys

N = int(sys.stdin.readline())
RGB_list = [[int(i) for i in sys.stdin.readline().split()] for _ in range(N)]

for i in range(1,len(RGB_list)):
    RGB_list[i][0] += min(RGB_list[i-1][1], RGB_list[i-1][2])
    RGB_list[i][1] += min(RGB_list[i-1][0], RGB_list[i-1][2])
    RGB_list[i][2] += min(RGB_list[i-1][0], RGB_list[i-1][1])

print(min(RGB_list[N-1]))