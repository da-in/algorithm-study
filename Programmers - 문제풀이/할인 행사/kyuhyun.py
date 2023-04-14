def solution(want, number, discount):
    answer = 0
    dic = {}

    for i in range(len(want)):
        dic[want[i]] = number[i]

    for i in range(len(discount) - 9):
        temp = dic.copy()
        day_dis = discount[i:i+10]

        for val in day_dis:
            if val in temp:
                temp[val] -= 1
                if temp[val] == 0:
                    temp.pop(val)
        if not temp:
            answer += 1
    return answer
