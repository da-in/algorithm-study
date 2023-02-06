def solution(numbers, target):
    answer = [0]
    for n in numbers:
        plus = list(map(lambda x: x + n, answer))
        minus = list(map(lambda x: x - n, answer))
        answer = plus + minus
    return answer.count(target)
