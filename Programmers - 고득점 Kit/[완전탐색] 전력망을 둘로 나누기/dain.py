from collections import defaultdict

def solution(n, wires):
    answer = n
    tree = defaultdict(list)

    for a, b in wires:
        tree[a].append(b)
        tree[b].append(a)

    for i in range(len(wires)):
        visit = [False for _ in range(n + 1)]
        a, b = wires[i]

        def dfs(cur):
            count = 1
            visit[cur] = True
            for next in tree[cur]:
                if not visit[next] and (cur, next) not in [(a, b), (b, a)]:
                    count += dfs(next)
            return count

        answer = min(answer, abs(dfs(a) - dfs(b)))

    return answer
