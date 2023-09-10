N = int(input())

answer = 0
st = []

for i in range(N) :
    x, y = map(int, input().split(" "))
    while st and st[-1] > y:
            answer += 1
            st.pop()
    if st and st[-1] == y:
        continue
    st.append(y)

while st:
    if st[-1] > 0:
        answer += 1
    st.pop()

print(answer)
        
