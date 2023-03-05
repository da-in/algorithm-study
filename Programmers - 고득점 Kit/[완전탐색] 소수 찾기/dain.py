from itertools import permutations
import math

def solution(numbers):
    permutation = []
    for i in range(1, len(numbers) + 1):
        permutation += list(
            map(lambda x: int("".join(x)), permutations(list(numbers), i))
        )

    permutation = list(set(permutation))  # 중복 제거
    isprime = [1] * len(permutation)

    for i in range(2, int(math.sqrt(max(permutation)) + 1)):
        for j in range(len(permutation)):
            if not isprime[j] or permutation[j] == i:
                continue
            if permutation[j] % i == 0 or permutation[j] == 0 or permutation[j] == 1:
                isprime[j] = 0

    return sum(isprime)
