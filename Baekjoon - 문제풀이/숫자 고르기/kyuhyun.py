N = int(input())

res_st = []
num = []

for i in range(N):
    num.append(int(input()))

cnt = 0
res = 0
for i in range(N) :
    visit = [0] * N
    st = [num[i]]

    while True:
        val = st[-1]
        # 원래 자리로 돌아오는 경우
        if val == i+1:
            break
        # 이미 방문한 노드로 돌아오는 경우
        if visit[val-1] == 1:
            st.clear()
            break
        if visit[val-1] == 0:
            visit[val-1] = 1
            st.append(num[val-1])

    if not st:
        continue
    res_st.extend(st)

res_st = list(set(res_st))
res_st.sort()
print(len(res_st))
print(*res_st, sep='\n')
