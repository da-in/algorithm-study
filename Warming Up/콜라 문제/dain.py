import sys
sys.setrecursionlimit(10**6)

def solution(a, b, n):
    def exchange(n):
        if n < a:
            return 0
        new = (n // a) * b
        left = n % a
        return new + exchange(new + left)

    return exchange(n)
