def solution(n,a,b):
    temp = n
    val = 0

    while temp > 1:
        temp //= 2
        val += 1

    while val:
        num = 2 ** (val-1)

        if ((a-1) // num) == ((b-1) // num):
            val -= 1
            continue
        else:
            return val
