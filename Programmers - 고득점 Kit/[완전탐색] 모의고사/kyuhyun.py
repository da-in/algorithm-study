def solution(answers):
    answer = []
    people_1 = [1, 2, 3, 4, 5]
    people_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count = [0] * 3


    for idx, num in enumerate(answers):
        if people_1[idx % 5] == num:
            count[0] += 1
        if people_2[idx % 8] == num:
            count[1] += 1
        if people_3[idx % 10] == num:
            count[2] += 1
            
    k = max(count)
    for i in range(3):
        if k == count[i]:
            answer.append(i+1)
    return answer
