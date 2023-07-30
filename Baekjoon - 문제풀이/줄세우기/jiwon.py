import sys

N = int(sys.stdin.readline())
child_list = [int(sys.stdin.readline()) for _ in range(N)]

for i in range(1,N+1):
    i_idx = child_list.index(i)
    child_list.remove(i)
    if i_idx>i-1:
        child_list = child_list[:i-1] + [i] + child_list[i-1:]


print(child_list)