def solution(N, number):
    if number == N:
        return 1
    num_set = [set() for _ in range(9)]
    num_set[1] = {N}
    for i in range(2, 9):
        for j in range(1, i):
            for k in num_set[j]:
                for l in num_set[i - j]:
                    num_set[i].add(k + l)
                    num_set[i].add(k - l)
                    num_set[i].add(k * l)
                    if l:
                        num_set[i].add(k // l)
                    num_set[i].add(int(str(N) * i))
        if number in num_set[i]:
            return i
    return -1
