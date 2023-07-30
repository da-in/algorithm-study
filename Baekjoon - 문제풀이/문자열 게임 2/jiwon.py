import sys

T = int(sys.stdin.readline())

for i in range(T):
    W = str(sys.stdin.readline().rstrip('\n'))
    K = int(sys.stdin.readline())
    
    for j in range(len(W)):
        s_idx = j
        