def solution(numbers):
    if not sum(numbers):
        return "0"
    numbers = list(map(lambda x: (str(x), str(x) * 4), numbers))
    numbers.sort(reverse=True, key=lambda x: (x[1][0], x[1][1], x[1][2], x[1][3]))
    numbers = list(map(lambda x: x[0], numbers))
    return "".join(numbers)
