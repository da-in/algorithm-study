"""
<풀이 시간>
3분

<input>
k : 1 ≤ K ≤ 100,000

<solution>
전형적인 stack 문제
1) 0이 입력되면, stack의 top을 제거
2) 0이 아닌 경우, 해당 수를 stack에 추가
3) 적어낸 수의 합을 sum(stack)으로 구할 수 있지만, 또 O(k)의 연산을 할 필요없이 입력값이 들어왔을 때 바로바로 갱신해주기
- 사소한 부분이지만 위 방식의 경우 84ms가 걸리고, sum(stack)의 경우 112ms가 걸렸음

"""
import sys
input = sys.stdin.readline

k = int(input()) # 1 ≤ K ≤ 100,000

ans = 0 # 최종적으로 적어낸 수의 합
stack = []
for _ in range(k):
    num = int(input()) # 정수
    if num == 0: # 가장 최근에 쓴 수를 지운다 -> stack의 top 제거
        ans -= stack.pop()
    else: # 0이 아니라면 해당 수를 쓴다 -> stack에 append
        stack.append(num)
        ans += num

print(ans)
