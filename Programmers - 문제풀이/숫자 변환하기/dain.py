def solution(x, y, n):
    answer = 0
    nums = {x}
    while nums:
        next = set()
        if y in nums:
            return answer
        for num in nums:
            if num + n <= y:
                next.add(num + n)
            if num * 2 <= y:
                next.add(num * 2)
            if num * 3 <= y:
                next.add(num * 3)
        nums = next
        answer += 1
    return -1
