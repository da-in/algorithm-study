def solution(arr):
    answer = []
    for n in arr:
        if not answer or answer[-1] != n:
            answer.append(n)
    return answer
